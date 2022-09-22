from django.shortcuts import render
from rest_framework.viewsets import ViewSet,ModelViewSet
from api.serializers import PostSerializer,UserSerializer,CommentSerializer
from rest_framework.response import Response
from api.models import Post
from rest_framework import authentication,permissions
from rest_framework.decorators import action
class PostsView(ViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def list(self,request,*args,**kwargs):
        qs=Post.objects.all()
        serializer=PostSerializer(qs,many=True)
        return Response(data=serializer.data)

    def create(self,request,*args,**kwargs):
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Post.objects.get(id=id)
        serializer=PostSerializer(qs)
        return Response(serializer.data)


    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        instance=Post.objects.get(id=id)
        serializer=PostSerializer(instance=instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        instance=Post.objects.get(id=id)
        instance.delete()
        return Response({"msg":"deleted"})

class UserView(ViewSet):
    def create(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

# Create your views here.
class PostModelView(ModelViewSet):
    serializer_class = PostSerializer
    queryset=Post.objects.all()
    #authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer=PostSerializer(data=request.data,context={"usr":request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
    @action(methods=["GET"],detail=False)
    def my_posts(self,request,*args,**kwargs):
        user=request.user
        qs=user.posts.all()
        serializer=PostSerializer(qs,many=True)
        return Response(data=serializer.data)
    @action(methods=["GET"],detail=True)
    def get_comments(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        post=Post.objects.get(id=id)
        comments=post.comments_set.all()
        serializer=CommentSerializer(comments,many=True)
        return Response(data=serializer.data)

    @action(methods=["POST"],detail=True)
    def add_comment(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        pst=Post.objects.get(id=id)
        serializer=CommentSerializer(data=request.data,context={"user":request.user,"post":pst})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    @action(methods=["POST"],detail=True)
    def add_like(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        pst=Post.objects.get(id=id)
        user=request.user
        pst.liked_by.add(user)
        return Response(data="ok")
    @action(methods=["GET"],detail=True)
    def get_likes(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        pst=Post.objects.get(id=id)
        cnt=pst.liked_by.all().count()
        return Response(data=cnt)
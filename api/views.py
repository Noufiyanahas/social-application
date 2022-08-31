from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from api.serializers import PostSerializer
from rest_framework.response import Response
from api.models import Post
class PostsView(ViewSet):
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

# Create your views here.

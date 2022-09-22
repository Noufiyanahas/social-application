from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="postimages",null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="posts")
    date= models.DateTimeField(auto_now_add=True)
    liked_by=models.ManyToManyField(User)
    def __str__(self):
        return self.title
    def like_count(self):
        return self.liked_by.all().count()

class Comments(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    comment=models.CharField(max_length=120)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments")

    def __str__(self):
        return self.comment

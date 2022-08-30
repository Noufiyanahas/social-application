from django.db import models

class Post(models.Model):
    title = models.Charfield(max_length=50)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="postimages",null=True)
    user=models.CharField(max_length=50)
    date= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

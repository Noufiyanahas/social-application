from api.models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Post
        exclude=("date",)
from rest_framework import serializers
from blog.models import Blog
class BogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id','title','content', 'user', 'category', 'slug' ]
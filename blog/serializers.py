# blog/serializers.py

from rest_framework import serializers
from .models import BlogCategory, Post

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['id', 'name', 'slug']

class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)
    categories_names = serializers.StringRelatedField(source='categories', many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'content', 'excerpt', 'image',
            'author', 'author_name', 'categories', 'categories_names',
            'tags', 'is_published', 'view_count', 'reading_time',
            'created_at', 'updated_at', 'published_at'
        ]
        read_only_fields = ['view_count', 'created_at', 'updated_at']
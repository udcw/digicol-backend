# community/serializers.py

from rest_framework import serializers
from .models import Post, Comment, Discussion
from accounts.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'author_name', 'content', 'created_at']
        read_only_fields = ['created_at']

class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Post
        fields = [
            'id', 'author', 'author_name', 'content', 'image',
            'likes', 'likes_count', 'comments', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at', 'likes_count']

class DiscussionSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)
    
    class Meta:
        model = Discussion
        fields = [
            'id', 'title', 'slug', 'content', 'author', 'author_name',
            'category', 'is_pinned', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
# community/admin.py

from django.contrib import admin
from .models import Post, Comment, Discussion

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'content_preview', 'likes_count', 'created_at']
    list_filter = ['created_at']
    search_fields = ['author__username', 'content']
    
    def content_preview(self, obj):
        return obj.content[:50] + '...'
    content_preview.short_description = 'Contenu'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created_at']
    list_filter = ['created_at']
    search_fields = ['author__username', 'content']

@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'is_pinned', 'created_at']
    list_filter = ['category', 'is_pinned']
    search_fields = ['title', 'content']
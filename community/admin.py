from django.contrib import admin
from .models import Post, Comment, Discussion

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created_at']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'post']

@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'category']
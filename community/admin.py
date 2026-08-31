from django.contrib import admin
from .models import Post, Comment, Discussion

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "author", "content_preview", "likes_count", "created_at"]
    def content_preview(self, obj):
        return obj.content[:50] + "..."
    content_preview.short_description = "Contenu"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "author", "post", "created_at"]

@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "author", "category", "is_pinned", "created_at"]

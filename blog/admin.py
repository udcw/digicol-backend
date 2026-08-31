from django.contrib import admin
from .models import BlogCategory, Post

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "author", "is_published", "created_at"]
    list_filter = ["is_published", "categories"]
    search_fields = ["title", "content"]
    filter_horizontal = ["categories"]

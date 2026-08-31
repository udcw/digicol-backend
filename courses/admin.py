from django.contrib import admin
from .models import Category, Course, Enrollment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "category", "level", "price", "is_published"]
    list_filter = ["category", "level", "is_published"]
    search_fields = ["title", "description"]

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ["id", "member", "course", "status", "enrollment_date"]
    list_filter = ["status"]

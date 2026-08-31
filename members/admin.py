from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name", "phone", "city", "domain", "is_active_member"]
    list_filter = ["city", "domain", "is_active_member"]
    search_fields = ["full_name", "phone", "skills"]

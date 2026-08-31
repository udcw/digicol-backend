from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'get_digicol_id', 'city', 'domain', 'is_active_member']
    list_filter = ['city', 'domain', 'is_active_member']
    search_fields = ['full_name', 'phone', 'skills']
    readonly_fields = ['qr_code']
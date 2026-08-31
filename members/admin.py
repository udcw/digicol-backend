# members/admin.py

from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    """Configuration de l'admin pour Member"""
    list_display = ('id', 'full_name', 'phone', 'city', 'domain', 'is_active_member', 'membership_date')
    list_filter = ('city', 'domain', 'is_active_member')
    search_fields = ('full_name', 'phone', 'skills', 'user__username', 'user__email')
    readonly_fields = ('membership_date',)
    
    fieldsets = (
        ('Informations personnelles', {
            'fields': ('user', 'full_name', 'phone', 'city', 'study_level', 'domain')
        }),
        ('Compétences et bio', {
            'fields': ('skills', 'bio')
        }),
        ('Photo et statut', {
            'fields': ('photo', 'is_active_member')
        }),
        ('Dates', {
            'fields': ('membership_date', 'updated_at')
        }),
    )
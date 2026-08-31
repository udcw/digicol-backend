# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'digicol_id', 'role', 'is_verified']
    list_filter = ['role', 'is_verified']
    search_fields = ['username', 'email', 'digicol_id']
    
    fieldsets = UserAdmin.fieldsets + (
        ('Informations DigiCol', {
            'fields': ('role', 'phone', 'avatar', 'digicol_id', 'is_verified'),
        }),
    )
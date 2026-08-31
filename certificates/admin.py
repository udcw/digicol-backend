from django.contrib import admin
from .models import Certificate

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['certificate_id', 'member', 'course', 'issue_date', 'is_verified']
    list_filter = ['is_verified']
    search_fields = ['certificate_id', 'member__full_name']
    readonly_fields = ['certificate_id', 'qr_code']
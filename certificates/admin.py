from django.contrib import admin
from .models import Certificate

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['id', 'certificate_id', 'member', 'course', 'issue_date']
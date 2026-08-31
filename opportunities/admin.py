# opportunities/admin.py

from django.contrib import admin
from .models import Opportunity

@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ['title', 'opportunity_type', 'company', 'deadline', 'is_published']
    list_filter = ['opportunity_type', 'is_published', 'is_remote']
    search_fields = ['title', 'company', 'description']
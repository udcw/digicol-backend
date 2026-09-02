from django.contrib import admin
from .models import Opportunity

@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'opportunity_type', 'company', 'deadline']
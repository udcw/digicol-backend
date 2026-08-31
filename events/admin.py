# events/admin.py

from django.contrib import admin
from .models import Event, EventRegistration

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_type', 'start_date', 'is_published']
    list_filter = ['event_type', 'is_published', 'is_free']
    search_fields = ['title', 'description']
    
    # Ajouter une méthode pour afficher is_full
    def get_is_full(self, obj):
        return obj.is_full
    get_is_full.boolean = True
    get_is_full.short_description = 'Complet'
    
    # OU utiliser list_display comme ceci:
    # list_display = ['title', 'event_type', 'start_date', 'is_published']

@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ['member', 'event', 'registration_date', 'is_confirmed']
    list_filter = ['is_confirmed', 'attended']
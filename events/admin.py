from django.contrib import admin
from .models import Event, EventRegistration

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "event_type", "start_date", "is_published"]
    list_filter = ["event_type", "is_published", "is_free"]
    search_fields = ["title", "description"]

@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ["id", "member", "event", "registration_date", "is_confirmed"]
    list_filter = ["is_confirmed", "attended"]

# events/serializers.py

from rest_framework import serializers
from .models import Event, EventRegistration

class EventSerializer(serializers.ModelSerializer):
    registrations_count = serializers.IntegerField(source='registrations.count', read_only=True)
    is_full = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Event
        fields = [
            'id', 'title', 'slug', 'event_type', 'description', 'image',
            'location', 'address', 'start_date', 'end_date',
            'max_participants', 'current_participants', 'price', 'is_free',
            'is_published', 'is_full', 'registrations_count',
            'created_by', 'created_at', 'updated_at'
        ]
        read_only_fields = ['current_participants', 'created_at', 'updated_at']

class EventRegistrationSerializer(serializers.ModelSerializer):
    member_name = serializers.CharField(source='member.full_name', read_only=True)
    event_title = serializers.CharField(source='event.title', read_only=True)
    
    class Meta:
        model = EventRegistration
        fields = [
            'id', 'event', 'event_title', 'member', 'member_name',
            'registration_date', 'is_confirmed', 'attended'
        ]
        read_only_fields = ['registration_date']
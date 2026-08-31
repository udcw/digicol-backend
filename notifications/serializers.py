# notifications/serializers.py

from rest_framework import serializers
from .models import Notification, Announcement

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            'id', 'recipient', 'notification_type', 'title',
            'message', 'link', 'is_read', 'created_at'
        ]
        read_only_fields = ['created_at']

class AnnouncementSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.username', read_only=True)
    
    class Meta:
        model = Announcement
        fields = [
            'id', 'title', 'content', 'is_active',
            'created_by', 'created_by_name', 'created_at', 'expires_at'
        ]
        read_only_fields = ['created_at']
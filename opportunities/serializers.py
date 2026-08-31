# opportunities/serializers.py

from rest_framework import serializers
from .models import Opportunity

class OpportunitySerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.username', read_only=True)
    
    class Meta:
        model = Opportunity
        fields = [
            'id', 'title', 'slug', 'opportunity_type', 'description',
            'requirements', 'location', 'is_remote', 'company',
            'contact_email', 'deadline', 'is_published',
            'created_by', 'created_by_name', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
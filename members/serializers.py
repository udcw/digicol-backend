# members/serializers.py

from rest_framework import serializers
from .models import Member
from accounts.serializers import UserSerializer

class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    digicol_id = serializers.CharField(source='user.digicol_id', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Member
        fields = [
            'id', 'user', 'username', 'email', 'digicol_id',
            'full_name', 'phone', 'city', 'study_level',
            'domain', 'skills', 'photo', 'bio',
            'is_active_member', 'membership_date', 'updated_at'
        ]
        read_only_fields = ['membership_date', 'updated_at']
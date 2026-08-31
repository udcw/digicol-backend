# certificates/serializers.py

from rest_framework import serializers
from .models import Certificate

class CertificateSerializer(serializers.ModelSerializer):
    member_name = serializers.CharField(source='member.full_name', read_only=True)
    course_title = serializers.CharField(source='course.title', read_only=True)
    
    class Meta:
        model = Certificate
        fields = [
            'id', 'certificate_id', 'member', 'member_name',
            'course', 'course_title', 'enrollment',
            'issue_date', 'expiry_date', 'pdf_file', 'qr_code', 'is_verified'
        ]
        read_only_fields = ['certificate_id', 'issue_date', 'qr_code', 'is_verified']
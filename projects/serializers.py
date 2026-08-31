# projects/serializers.py

from rest_framework import serializers
from .models import Project
from members.serializers import MemberSerializer

class ProjectSerializer(serializers.ModelSerializer):
    team_members = MemberSerializer(source='team', many=True, read_only=True)
    created_by_name = serializers.CharField(source='created_by.username', read_only=True)
    team_ids = serializers.ListField(child=serializers.IntegerField(), write_only=True, required=False)
    
    class Meta:
        model = Project
        fields = [
            'id', 'title', 'slug', 'description', 'technologies',
            'image', 'github_url', 'demo_url', 'status',
            'team', 'team_members', 'team_ids', 'team_size',
            'created_by', 'created_by_name',
            'start_date', 'end_date', 'created_at', 'updated_at'
        ]
        read_only_fields = ['team_size', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        team_ids = validated_data.pop('team_ids', [])
        project = Project.objects.create(**validated_data)
        if team_ids:
            from members.models import Member
            members = Member.objects.filter(id__in=team_ids)
            project.team.set(members)
        return project
# courses/serializers.py

from rest_framework import serializers
from .models import Category, Course, Enrollment

class CategorySerializer(serializers.ModelSerializer):
    course_count = serializers.IntegerField(source='courses.count', read_only=True)
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'icon', 'description', 'course_count']

class CourseSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    instructor_name = serializers.CharField(source='instructor.username', read_only=True)
    enrollment_count = serializers.IntegerField(source='enrollments.count', read_only=True)
    
    class Meta:
        model = Course
        fields = [
            'id', 'title', 'slug', 'category', 'category_name',
            'description', 'image', 'level', 'duration', 'program',
            'prerequisites', 'instructor', 'instructor_name',
            'price', 'available_seats', 'is_published',
            'start_date', 'end_date', 'is_available', 'enrollment_count',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['is_available', 'created_at', 'updated_at']

class EnrollmentSerializer(serializers.ModelSerializer):
    member_name = serializers.CharField(source='member.full_name', read_only=True)
    course_title = serializers.CharField(source='course.title', read_only=True)
    
    class Meta:
        model = Enrollment
        fields = [
            'id', 'member', 'member_name', 'course', 'course_title',
            'status', 'enrollment_date', 'completion_date', 'certificate_generated'
        ]
        read_only_fields = ['enrollment_date']
# courses/views.py

from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Course, Enrollment
from .serializers import CategorySerializer, CourseSerializer, EnrollmentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

class CategoryListCreateView(generics.ListCreateAPIView):
    """Liste et création des catégories"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Détail, modification, suppression d'une catégorie"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CourseListCreateView(generics.ListCreateAPIView):
    """Liste et création des formations"""
    queryset = Course.objects.filter(is_published=True)
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'level', 'is_published']
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'created_at']

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Détail, modification, suppression d'une formation"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class EnrollmentListCreateView(generics.ListCreateAPIView):
    """Liste et création des inscriptions"""
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Enrollment.objects.filter(member__user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(member=self.request.user.member_profile)

class EnrollmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Détail, modification, suppression d'une inscription"""
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Enrollment.objects.filter(member__user=self.request.user)
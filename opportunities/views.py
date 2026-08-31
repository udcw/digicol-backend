# opportunities/views.py

from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Opportunity
from .serializers import OpportunitySerializer

class OpportunityListCreateView(generics.ListCreateAPIView):
    queryset = Opportunity.objects.filter(is_published=True)
    serializer_class = OpportunitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['opportunity_type', 'is_remote']
    search_fields = ['title', 'company', 'description']

class OpportunityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
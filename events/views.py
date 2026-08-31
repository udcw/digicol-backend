# events/views.py

from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Event, EventRegistration
from .serializers import EventSerializer, EventRegistrationSerializer

class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.filter(is_published=True)
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['event_type', 'is_free']
    search_fields = ['title', 'description']

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EventRegistrationListCreateView(generics.ListCreateAPIView):
    serializer_class = EventRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return EventRegistration.objects.filter(member__user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(member=self.request.user.member_profile)
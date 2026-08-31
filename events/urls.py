# events/urls.py

from django.urls import path
from .views import EventListCreateView, EventDetailView, EventRegistrationListCreateView

urlpatterns = [
    path('', EventListCreateView.as_view(), name='event-list'),
    path('<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('registrations/', EventRegistrationListCreateView.as_view(), name='event-registration-list'),
]
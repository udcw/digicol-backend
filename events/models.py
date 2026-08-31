# events/models.py

from django.db import models
from django.conf import settings

class Event(models.Model):
    TYPE_CHOICES = [
        ('WORKSHOP', 'Atelier'),
        ('CONFERENCE', 'Conférence'),
        ('BOOTCAMP', 'Bootcamp'),
        ('HACKATHON', 'Hackathon'),
        ('MEETUP', 'Rencontre'),
        ('FORMATION', 'Formation'),
    ]
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    event_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='events/images/', blank=True, null=True)
    location = models.CharField(max_length=255)
    address = models.TextField(blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    max_participants = models.IntegerField(default=50)
    current_participants = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    is_free = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='events_created'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    member = models.ForeignKey('members.Member', on_delete=models.CASCADE, related_name='event_registrations')
    registration_date = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)
    attended = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ['event', 'member']
    
    def __str__(self):
        return f"{self.member.full_name} - {self.event.title}"
# opportunities/models.py

from django.db import models
from django.conf import settings

class Opportunity(models.Model):
    TYPE_CHOICES = [
        ('STAGE', 'Stage'),
        ('EMPLOI', 'Emploi'),
        ('FREELANCE', 'Freelance'),
        ('HACKATHON', 'Hackathon'),
        ('FORMATION', 'Formation'),
        ('PROJET', 'Projet'),
    ]
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    opportunity_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField()
    requirements = models.TextField()
    location = models.CharField(max_length=255)
    is_remote = models.BooleanField(default=False)
    company = models.CharField(max_length=255, blank=True)
    contact_email = models.EmailField()
    deadline = models.DateTimeField()
    is_published = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='opportunities_created'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
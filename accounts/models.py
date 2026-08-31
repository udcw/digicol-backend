# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

class User(AbstractUser):
    ROLE_CHOICES = [
        ('SUPER_ADMIN', 'Super Admin'),
        ('ADMIN', 'Admin'),
        ('FORMATEUR', 'Formateur'),
        ('MODERATEUR', 'Modérateur'),
        ('MEMBRE', 'Membre'),
        ('VISITEUR', 'Visiteur'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='MEMBRE')
    phone = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.URLField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    digicol_id = models.CharField(max_length=50, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.digicol_id:
            year = datetime.now().year
            count = User.objects.filter(digicol_id__startswith=f'DIGICOL-MEM-{year}').count() + 1
            self.digicol_id = f'DIGICOL-MEM-{year}-{count:03d}'
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.username} ({self.digicol_id})"
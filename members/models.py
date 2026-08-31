# members/models.py

from django.db import models
from django.conf import settings

class Member(models.Model):
    """Profil complet du membre DigiCol"""
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='member_profile'
    )
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, default='')
    city = models.CharField(max_length=100, blank=True, default='')
    study_level = models.CharField(max_length=100, blank=True, default='')
    domain = models.CharField(max_length=100, blank=True, default='')
    skills = models.TextField(blank=True, default='')
    photo = models.ImageField(upload_to='members/photos/', blank=True, null=True)
    bio = models.TextField(blank=True, default='')
    is_active_member = models.BooleanField(default=True)
    membership_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.full_name
    
    def get_digicol_id(self):
        """Récupère l'ID DigiCol de l'utilisateur"""
        return self.user.digicol_id if self.user else None
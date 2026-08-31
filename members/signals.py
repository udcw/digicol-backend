# members/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Member

User = get_user_model()

@receiver(post_save, sender=User)
def create_member_profile(sender, instance, created, **kwargs):
    """Crée automatiquement un Member lors de l'inscription d'un utilisateur"""
    if created:
        Member.objects.create(
            user=instance,
            full_name=f"{instance.first_name} {instance.last_name}".strip() or instance.username,
            phone=instance.phone or '',
            city='',
            study_level='',
            domain='',
            skills='',
            is_active_member=True
        )
        print(f" Profil Member créé pour {instance.username}")

@receiver(post_save, sender=User)
def save_member_profile(sender, instance, **kwargs):
    """Sauvegarde le Member quand l'utilisateur est sauvegardé"""
    # Vérifier si le Member existe, sinon le créer
    try:
        instance.member_profile.save()
    except Member.DoesNotExist:
        Member.objects.create(
            user=instance,
            full_name=f"{instance.first_name} {instance.last_name}".strip() or instance.username,
            phone=instance.phone or '',
            is_active_member=True
        )
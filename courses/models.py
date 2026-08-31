# courses/models.py

from django.db import models
from django.conf import settings
from django.utils import timezone

class Category(models.Model):
    """Catégorie de formation"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=50, blank=True, help_text="Nom de l'icône FontAwesome")
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    """Formation DigiCol"""
    
    LEVEL_CHOICES = [
        ('DEBUTANT', 'Débutant'),
        ('INTERMEDIAIRE', 'Intermédiaire'),
        ('AVANCE', 'Avancé'),
        ('EXPERT', 'Expert'),
    ]
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    description = models.TextField()
    image = models.ImageField(upload_to='courses/images/', blank=True, null=True)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='DEBUTANT')
    duration = models.CharField(max_length=50, help_text="Ex: 2 jours, 4 semaines")
    program = models.TextField(help_text="Programme détaillé")
    prerequisites = models.TextField(blank=True)
    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='courses_taught'
    )
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    available_seats = models.IntegerField(default=10)
    is_published = models.BooleanField(default=False)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    @property
    def is_available(self):
        return self.available_seats > 0 and self.is_published

class Enrollment(models.Model):
    """Inscription à une formation"""
    
    STATUS_CHOICES = [
        ('PENDING', 'En attente'),
        ('CONFIRMED', 'Confirmé'),
        ('COMPLETED', 'Terminé'),
        ('CANCELLED', 'Annulé'),
    ]
    
    member = models.ForeignKey('members.Member', on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    enrollment_date = models.DateTimeField(auto_now_add=True)
    completion_date = models.DateTimeField(null=True, blank=True)
    certificate_generated = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ['member', 'course']
    
    def __str__(self):
        return f"{self.member.full_name} - {self.course.title}"
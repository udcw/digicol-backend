# community/models.py

from django.db import models
from django.conf import settings

class Post(models.Model):
    """Publication dans la communauté"""
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='community_posts'
    )
    content = models.TextField()
    image = models.ImageField(upload_to='community/posts/', blank=True, null=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.author.username} - {self.content[:50]}"
    
    @property
    def likes_count(self):
        return self.likes.count()

class Comment(models.Model):
    """Commentaire sur une publication"""
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.author.username} - {self.content[:30]}"

class Discussion(models.Model):
    """Discussion communautaire"""
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='discussions')
    category = models.CharField(max_length=100, choices=[
        ('TECH', 'Technologie'),
        ('PROJET', 'Projets'),
        ('CARRIERE', 'Carrière'),
        ('FORMATION', 'Formation'),
        ('GENERAL', 'Général'),
    ])
    is_pinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
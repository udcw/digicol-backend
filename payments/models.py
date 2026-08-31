# payments/models.py

from django.db import models
from django.conf import settings

class Wallet(models.Model):
    """Portefeuille DigiCol d'un membre"""
    
    member = models.OneToOneField(
        'members.Member',
        on_delete=models.CASCADE,
        related_name='wallet'
    )
    balance = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Wallet de {self.member.full_name} - {self.balance} FCFA"

class Transaction(models.Model):
    """Transaction financière"""
    
    TYPE_CHOICES = [
        ('CREDIT', 'Crédit'),
        ('DEBIT', 'Débit'),
    ]
    
    STATUS_CHOICES = [
        ('PENDING', 'En attente'),
        ('COMPLETED', 'Terminé'),
        ('FAILED', 'Échoué'),
        ('CANCELLED', 'Annulé'),
    ]
    
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=12, decimal_places=0)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    reference = models.CharField(max_length=100, unique=True, blank=True, null=True)
    payment_method = models.CharField(max_length=50, blank=True, null=True)
    external_reference = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.get_transaction_type_display()} - {self.amount} FCFA - {self.status}"

class PaymentMethod(models.Model):
    """Méthode de paiement configurée"""
    
    PAYMENT_METHODS = [
        ('ORANGE', 'Orange Money'),
        ('MTN', 'MTN Mobile Money'),
        ('STRIPE', 'Stripe'),
        ('MANUAL', 'Manuel'),
    ]
    
    name = models.CharField(max_length=50, choices=PAYMENT_METHODS)
    is_active = models.BooleanField(default=True)
    api_key = models.CharField(max_length=255, blank=True)
    api_secret = models.CharField(max_length=255, blank=True)
    webhook_secret = models.CharField(max_length=255, blank=True)
    is_sandbox = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.get_name_display()} - {'Sandbox' if self.is_sandbox else 'Production'}"
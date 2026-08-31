# payments/admin.py

from django.contrib import admin
from .models import Wallet, Transaction, PaymentMethod

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ['member', 'balance', 'created_at']
    search_fields = ['member__full_name']
    readonly_fields = ['balance']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['wallet', 'transaction_type', 'amount', 'status', 'created_at']
    list_filter = ['transaction_type', 'status']
    search_fields = ['wallet__member__full_name', 'description', 'reference']

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'is_sandbox']
    list_filter = ['is_active', 'is_sandbox']
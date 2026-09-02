from django.contrib import admin
from .models import Wallet, Transaction, PaymentMethod

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ['id', 'member', 'balance']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'wallet', 'amount', 'status']

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active']
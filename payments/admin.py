from django.contrib import admin
from .models import Wallet, Transaction, PaymentMethod

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ["id", "member", "balance", "created_at"]

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ["id", "wallet", "transaction_type", "amount", "status", "created_at"]
    list_filter = ["transaction_type", "status"]

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_active", "is_sandbox"]
    list_filter = ["is_active", "is_sandbox"]

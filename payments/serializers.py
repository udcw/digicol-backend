# payments/serializers.py

from rest_framework import serializers
from .models import Wallet, Transaction, PaymentMethod
from members.serializers import MemberSerializer

class WalletSerializer(serializers.ModelSerializer):
    member_name = serializers.CharField(source='member.full_name', read_only=True)
    
    class Meta:
        model = Wallet
        fields = ['id', 'member', 'member_name', 'balance', 'created_at', 'updated_at']
        read_only_fields = ['balance', 'created_at', 'updated_at']

class TransactionSerializer(serializers.ModelSerializer):
    wallet_owner = serializers.CharField(source='wallet.member.full_name', read_only=True)
    
    class Meta:
        model = Transaction
        fields = [
            'id', 'wallet', 'wallet_owner', 'transaction_type', 'amount',
            'description', 'status', 'reference', 'payment_method',
            'external_reference', 'created_at', 'completed_at'
        ]
        read_only_fields = ['reference', 'created_at', 'completed_at']

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['id', 'name', 'is_active', 'is_sandbox']
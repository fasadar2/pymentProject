from rest_framework import serializers
from rest_framework.fields import CharField,IntegerField

from .models import Wallet


class OperationSerializer(serializers.Serializer):
    OPERATION_CHOICES = (
        ("DEPOSIT", "DEPOSIT"),
        ("WITHDRAW", "WITHDRAW"),
    )
    operation_type = CharField(
        help_text="Тип операции: только 'DEPOSIT' (пополнение) или 'WITHDRAW' (снятие)",
    )
    amount = IntegerField()

    def validate_operation_type(self, value):
        allowed = {"DEPOSIT", "WITHDRAW"}
        if value not in allowed:
            raise serializers.ValidationError(f"operation_type must be one of {allowed}")
        return value


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ["id", "balance"]
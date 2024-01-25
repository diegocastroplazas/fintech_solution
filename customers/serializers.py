from rest_framework import serializers

from .data import CUSTOMER_STATUS_CHOICES
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """Customer serializer"""

    status = serializers.ChoiceField(choices=CUSTOMER_STATUS_CHOICES, default=1)

    class Meta:
        model = Customer
        fields = (
            "id",
            "external_id",
            "created_at",
            "updated_at",
            "score",
            "pre_approved_at",
            "status",
        )
        read_only_fields = ("id", "created_at", "updated_at")


class CustomerBalanceSerializer(serializers.ModelSerializer):
    """Customer balance serializer"""

    class Meta:
        model = Customer
        fields = ("external_id", "score", "total_debt", "available_amount")
        read_only_fields = ("external_id", "score", "total_debt", "available_amount")

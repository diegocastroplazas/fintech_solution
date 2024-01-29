from rest_framework import serializers
from .models import Loan
from customers.models import Customer
from django.shortcuts import get_object_or_404


class LoanBaseSerializer(serializers.ModelSerializer):
    outstanding = serializers.DecimalField(
        source="outstanding_amount", max_digits=12, decimal_places=2
    )

    class Meta:
        model = Loan
        fields = (
            "external_id",
            "amount",
            "outstanding",
            "status",
            "maximum_payment_date",
            "customer_external_id",
        )


class LoanCreateSerializer(LoanBaseSerializer):
    """Loan serializer"""

    customer_external_id = serializers.CharField(write_only=True)

    def create(self, validated_data):
        customer_external_id = validated_data.pop("customer_external_id")
        costumer = get_object_or_404(Customer, external_id=customer_external_id)
        validated_data["customer"] = costumer
        return Loan.objects.create(**validated_data)


class LoanReadSerializer(LoanBaseSerializer):
    """Loan serializer"""

    customer_external_id = serializers.CharField(source="customer.external_id")

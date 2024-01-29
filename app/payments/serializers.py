from rest_framework import serializers
from .models import Payment, PaymentDetail
from django.shortcuts import get_object_or_404
from customers.models import Customer


class PaymentBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            "external_id",
            "total_amount",
            "customer_external_id",
            "status",
        )


class PaymentCreateSerializer(PaymentBaseSerializer):
    """Loan serializer"""

    customer_external_id = serializers.SlugRelatedField(
        slug_field="external_id", queryset=Customer.objects.all(), write_only=True
    )

    def create(self, validated_data):
        customer_external_id = validated_data.pop("customer_external_id")
        customer = customer_external_id
        return Payment.objects.create(**validated_data, customer=customer)


class PaymentReadSerializer(PaymentBaseSerializer):
    """Loan serializer"""

    customer_external_id = serializers.CharField(source="customer.external_id")


class PaymentDetailSerializer(serializers.ModelSerializer):
    """PaymentDetail serializer"""

    fee = serializers.DecimalField(max_digits=20, decimal_places=10, default=0.19)

    class Meta:
        model = PaymentDetail
        fields = ("payment", "loan", "amount", "fee")

from rest_framework import serializers


from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """Customer serializer"""

    status = serializers.ChoiceField(
        choices=Customer.Status.choices, default=Customer.Status.ACTIVE
    )

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

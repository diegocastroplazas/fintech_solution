from rest_framework import serializers

from .models import Customer
from .data import COSTUMER_STATUS_CHOICES


class CustomerSerializer(serializers.ModelSerializer):
    """Customer serializer"""

    status = serializers.ChoiceField(choices=COSTUMER_STATUS_CHOICES, default=1)

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

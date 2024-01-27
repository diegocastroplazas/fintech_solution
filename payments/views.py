from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Payment
from loans.models import Loan
from .serializers import (
    PaymentCreateSerializer,
    PaymentDetailSerializer,
    PaymentReadSerializer,
)


class PaymentsView(APIView):
    """Payments view"""

    def get(self, request, *args, **kwargs):
        payments = Payment.objects.all()
        serializer = PaymentReadSerializer(payments, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        payment_serializer = PaymentCreateSerializer(data=request.data)
        payment_serializer.is_valid(raise_exception=True)
        payment = payment_serializer.save()

        loans = Loan.objects.filter(customer=payment.customer)

        for loan in loans:
            serializer = PaymentDetailSerializer(
                data={
                    "payment": payment.id,
                    "loan": loan.id,
                    "amount": payment.total_amount,
                }
            )
            serializer.is_valid(raise_exception=True)

        return Response(payment_serializer.data, status=status.HTTP_201_CREATED)

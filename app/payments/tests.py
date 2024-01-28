from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Payment
from customers.models import Customer
from .serializers import PaymentReadSerializer
from datetime import datetime
from loans.models import Loan
from fintech_solution.test import BaseTestCase


class PaymentsViewTestCase(BaseTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.customer = Customer.objects.create(
            external_id="1234567890", score=500.00, pre_approved_at=datetime.now()
        )
        cls.loan = Loan.objects.create(
            customer=cls.customer,
            amount=1000,
            status=Loan.Status.PENDING,
            contract_version="1.0",
            maximum_payment_date=datetime.now(),
            taken_at=datetime.now(),
            outstanding_amount=1000,
            external_id="loan-01",
        )
        cls.payment = Payment.objects.create(
            external_id="0987654321",
            customer=cls.customer,
            paid_at=datetime.now(),
            total_amount=1000,
        )

    def setUp(self):
        super().setUp()
        self.url = reverse("payments")

    def test_get_all_payments(self):
        response = self.client.get(self.url)
        payments = Payment.objects.all()
        serializer = PaymentReadSerializer(payments, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_payment(self):
        data = {
            "external_id": "external_01-02",
            "customer_external_id": "1234567890",
            "payment_date": "2023-06-12",
            "status": 1,
            "total_amount": 1000,
            "payment_amount": 500,
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Payment.objects.count(), 2)
        self.assertEqual(Payment.objects.get(id=2).total_amount, 1000.00)

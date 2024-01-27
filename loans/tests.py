from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Loan
from customers.models import Customer
from .serializers import LoanReadSerializer
from datetime import datetime


class LoansViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.customer = Customer.objects.create(
            external_id="1234567890",
            score=500.00,
            pre_approved_at=datetime.now(),
        )
        self.loan = Loan.objects.create(
            customer=self.customer,
            amount=1000,
            status=Loan.Status.PENDING,
            contract_version="1.0",
            maximum_payment_date=datetime.now(),
            taken_at=datetime.now(),
            outstanding_amount=1000,
        )
        self.url = reverse("loans")

    def test_get_all_loans(self):
        response = self.client.get(self.url)
        loans = Loan.objects.all()
        serializer = LoanReadSerializer(loans, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

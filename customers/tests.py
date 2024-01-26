from rest_framework.test import APITestCase
from customers.models import Customer
from django.urls import reverse
from rest_framework import status
from decimal import Decimal
from datetime import datetime


class CustomersViewTestCase(APITestCase):
    def setUp(self):
        Customer.objects.create(
            external_id="1234567890",
            score=Decimal("500.00"),
            pre_approved_at=datetime.now(),
        )

    def test_get_customer_list(self):
        url = reverse("customers")
        response = self.client.get(url)
        customer = Customer.objects.get(external_id="1234567890")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["external_id"], customer.external_id)
        self.assertEqual(response.data[0]["score"], str(customer.score))
        self.assertEqual(
            response.data[0]["pre_approved_at"],
            customer.pre_approved_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        )

    def test_create_customer(self):
        url = reverse("customers")
        data = {
            "external_id": "0987654321",
            "score": "600.00",
            "pre_approved_at": "2020-01-01T00:00:00.000000Z",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 2)
        last_costumer = Customer.objects.last()
        self.assertEqual(last_costumer.external_id, "0987654321")
        self.assertEqual(last_costumer.score, Decimal("600.00"))
        self.assertEqual(
            last_costumer.pre_approved_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            "2020-01-01T00:00:00.000000Z",
        )
        self.assertTrue(last_costumer.status == Customer.Status.ACTIVE)

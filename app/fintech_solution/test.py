from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User


class BaseTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)

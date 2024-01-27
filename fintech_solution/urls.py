from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("api/customers/", include("customers.urls")),
    path("api/loans/", include("loans.urls")),
    path("api/payments/", include("payments.urls")),
]

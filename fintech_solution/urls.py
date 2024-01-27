from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/customers/", include("customers.urls")),
    path("api/loans/", include("loans.urls")),
    path("api/payments/", include("payments.urls")),
]

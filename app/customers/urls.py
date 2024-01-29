from django.urls import path

from . import views

urlpatterns = [
    path("", views.CustomersView.as_view(), name="customers"),
    path(
        "<int:pk>/balance/",
        views.CustomerBalanceView.as_view(),
        name="customer-balance",
    ),
]

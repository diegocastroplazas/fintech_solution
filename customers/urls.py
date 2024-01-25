from django.urls import path

from . import views

urlpatterns = [
    path("", views.CustomersView.as_view()),
    path("<int:pk>/balance/", views.CustomerBalanceView.as_view()),
]

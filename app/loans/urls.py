from django.urls import path

from . import views

urlpatterns = [
    path("", views.LoansView.as_view(), name="loans"),
]

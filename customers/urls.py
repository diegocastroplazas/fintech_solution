from django.urls import path
from . import views

urlpatterns = [
    path("", views.CostumersView.as_view()),
]

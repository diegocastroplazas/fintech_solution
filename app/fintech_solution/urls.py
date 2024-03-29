from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)


urlpatterns = [
    path(
        "",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("admin/", admin.site.urls),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("api/customers/", include("customers.urls")),
    path("api/loans/", include("loans.urls")),
    path("api/payments/", include("payments.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
]

from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

api_info = openapi.Info(
    title="ALX Travel App API",
    default_version="v1",
    description="Auto-generated Swagger documentation for ALX Travel App.",
)

SchemaView = get_schema_view(
    api_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # Listings API routes (example)
    path("api/", include("listings.urls")),

    # Swagger UI
    path("swagger/", SchemaView.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    # Optional: ReDoc
    path("redoc/", SchemaView.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

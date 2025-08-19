from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExampleListingViewSet

router = DefaultRouter()
router.register(r"examples", ExampleListingViewSet, basename="examplelisting")

urlpatterns = [
    path("", include(router.urls)),
]

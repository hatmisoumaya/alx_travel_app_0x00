from rest_framework import viewsets, permissions
from .models import ExampleListing
from .serializers import ExampleListingSerializer

class ExampleListingViewSet(viewsets.ModelViewSet):
    queryset = ExampleListing.objects.all()
    serializer_class = ExampleListingSerializer
    permission_classes = [permissions.AllowAny]

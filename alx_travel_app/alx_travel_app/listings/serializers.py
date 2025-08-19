from rest_framework import serializers
from .models import ExampleListing

class ExampleListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleListing
        fields = ["id", "title", "created_at"]

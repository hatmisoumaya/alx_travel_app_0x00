from django.test import TestCase
from .models import ExampleListing

class ExampleListingTest(TestCase):
    def test_create(self):
        item = ExampleListing.objects.create(title="Hello")
        self.assertTrue(item.id)

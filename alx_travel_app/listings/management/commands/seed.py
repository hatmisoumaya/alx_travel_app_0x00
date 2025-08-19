from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        if Listing.objects.exists():
            self.stdout.write(self.style.WARNING("Listings already exist, skipping."))
            return

        User.objects.get_or_create(username="demo_user", defaults={"email": "demo@example.com"})

        sample = [
            {"title": "Beachfront Villa", "description": "Sea view", "price_per_night": 120.00, "location": "Malibu"},
            {"title": "Mountain Cabin", "description": "Cozy and quiet", "price_per_night": 80.00, "location": "Aspen"},
            {"title": "City Apartment", "description": "Downtown modern", "price_per_night": 100.00, "location": "New York"},
        ]
        for item in sample:
            Listing.objects.create(**item)

        self.stdout.write(self.style.SUCCESS("Seeded database with sample listings."))

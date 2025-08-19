from django.contrib import admin
from .models import ExampleListing

@admin.register(ExampleListing)
class ExampleListingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at")

# ALX Travel App 0x00

## Overview
This project is part of **Milestone 2** of the ALX Travel App backend.

It adds:
- Database models: Listing, Booking, Review
- DRF serializers for Listing and Booking
- A custom Django management command (`seed`) to populate the database with sample listings

## How to run
```bash
# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Seed the database with sample data
python manage.py seed

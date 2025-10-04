from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("customer", "course", "scheduled_date", "is_paid", "booking_date")
    list_filter = ("is_paid", "scheduled_date", "booking_date")
    search_fields = ("customer__full_name", "course__title")

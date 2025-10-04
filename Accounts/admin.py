from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "date_joined")
    search_fields = ("full_name", "email")
    list_filter = ("date_joined",)

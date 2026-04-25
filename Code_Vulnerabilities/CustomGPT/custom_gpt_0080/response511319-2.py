
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Calculate rent_price based on mrp (e.g., setting it to 90% of mrp)
        obj.rent_price = obj.mrp * 0.9  # Change this logic as needed
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)


from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Calculate rent_price based on mrp (e.g., 10% of mrp)
        obj.rent_price = obj.mrp * 0.10  # Example calculation
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

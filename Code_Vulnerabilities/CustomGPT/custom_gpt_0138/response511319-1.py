
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Calculate the rent_price based on mrp (e.g., 10% of MRP as an example)
        obj.rent_price = obj.mrp * 0.9  # Adjust this calculation as needed
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)


# admin.py
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, change):
        # Calculate the rent_price based on mrp; for example, 10% of mrp
        if obj.mrp:
            obj.rent_price = obj.mrp * 0.10  # Adjust the calculation as needed
        super().save_model(request, obj, change)

admin.site.register(Book, BookAdmin)

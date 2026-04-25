
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, change):
        # Calculate rent price based on mrp
        if obj.mrp:
            obj.rent_price = obj.mrp * 0.1  # Example: rent is 10% of MRP
        super().save_model(request, obj, change)

admin.site.register(Book, BookAdmin)

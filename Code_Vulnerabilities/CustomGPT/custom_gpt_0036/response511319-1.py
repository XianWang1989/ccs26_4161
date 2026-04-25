
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if obj.mrp:
            # Example calculation for rent_price based on mrp
            obj.rent_price = obj.mrp * 0.1  # Let's say rent price is 10% of MRP
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

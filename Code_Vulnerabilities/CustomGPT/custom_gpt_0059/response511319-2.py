
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Set rent_price based on mrp; apply any calculation logic you need here
        obj.rent_price = obj.mrp * 0.1  # Example: 10% of MRP
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

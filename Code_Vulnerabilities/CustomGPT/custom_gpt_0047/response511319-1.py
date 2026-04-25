
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Calculate rent_price based on mrp (example: 10% of MRP)
        obj.rent_price = obj.mrp * 0.1  # Or any calculation you'd like
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

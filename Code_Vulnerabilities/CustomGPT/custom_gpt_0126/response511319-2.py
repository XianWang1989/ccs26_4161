
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, change):
        # Auto-calculate rent_price based on mrp
        obj.rent_price = obj.mrp * 0.1  # Example calculation; adjust as needed
        super().save_model(request, obj, change)

admin.site.register(Book, BookAdmin)

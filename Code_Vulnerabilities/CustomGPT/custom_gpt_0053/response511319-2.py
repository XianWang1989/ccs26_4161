
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Define which fields to display in the admin
    fields = ['mrp', 'rent_price']

    def save_model(self, request, obj, form, change):
        # Calculate rent_price based on mrp
        if obj.mrp:
            obj.rent_price = obj.mrp * 0.1  # Example calculation (10% of MRP)
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)


from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('mrp', 'rent_price')  # Display fields in the list view

    def save_model(self, request, obj, form, change):
        if obj.mrp:
            # Calculate rent_price based on mrp; adjust the logic as needed
            obj.rent_price = obj.mrp * 0.8  # Example calculation (20% discount)
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

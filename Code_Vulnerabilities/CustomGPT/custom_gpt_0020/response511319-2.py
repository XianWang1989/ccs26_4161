
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('mrp', 'rent_price')  # Display fields in the admin list view

    def save_model(self, request, obj, form, change):
        # Calculate rent_price based on mrp
        if not obj.rent_price:
            obj.rent_price = obj.mrp * 0.1  # Example calculation here (10% of MRP)
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

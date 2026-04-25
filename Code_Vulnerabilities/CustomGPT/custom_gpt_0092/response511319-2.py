
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('mrp', 'rent_price')  # Display fields in admin

    def save_model(self, request, obj, form, change):
        if obj.mrp:  # Check if mrp has a value
            obj.rent_price = obj.mrp * 0.1  # Example calculation
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

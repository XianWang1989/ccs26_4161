
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('mrp', 'rent_price')

    def save_model(self, request, obj, form, change):
        # Calculate rent_price based on mrp. For example, rent_price = mrp * 0.1
        obj.rent_price = obj.mrp * 0.1  # Adjust the calculation as needed
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

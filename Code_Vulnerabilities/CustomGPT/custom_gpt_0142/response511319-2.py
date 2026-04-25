
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Calculate rent_price based on mrp
        # For example, let's say rent_price is 10% of mrp
        obj.rent_price = obj.mrp * 0.10  # Change the formula as needed
        super().save_model(request, obj, form, change)

    list_display = ('mrp', 'rent_price')  # Display these fields in the admin list view

admin.site.register(Book, BookAdmin)

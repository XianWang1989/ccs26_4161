
# admin.py
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Define your model admin interface as needed
    list_display = ('mrp', 'rent_price',)

    def save_model(self, request, obj, form, change):
        # Calculate rent_price based on mrp
        if obj.mrp:
            obj.rent_price = round(obj.mrp * 0.1, 2)  # For example, rent is 10% of mrp
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)


# admin.py
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Other admin configurations can be added here

    def save_model(self, request, obj, form, change):
        # Calculate the rent_price based on the mrp
        if obj.mrp:
            # For example, we can set rent_price to 10% of mrp
            obj.rent_price = obj.mrp * 0.10  # Calculate rent_price here

        # Call the parent class's save_model method to save the object
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

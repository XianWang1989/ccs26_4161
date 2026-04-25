
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ['mrp', 'rent_price']  # Display fields in the admin list view

    def save_model(self, request, obj, form, change):
        # Calculate rent_price based on mrp before saving
        if obj.mrp is not None:
            # Example calculation: rent_price is 10% of mrp
            obj.rent_price = round(obj.mrp * 0.1, 2)
        super().save_model(request, obj, form, change)  # Call the superclass method to save the object

admin.site.register(Book, BookAdmin)


from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Calculate the rent_price based on mrp
        if obj.mrp:
            obj.rent_price = obj.mrp * 0.1  # Adjust the calculation as needed
        super().save_model(request, obj, form, change)

    # Optional: to show the fields in the admin form
    fields = ('mrp', 'rent_price')

admin.site.register(Book, BookAdmin)

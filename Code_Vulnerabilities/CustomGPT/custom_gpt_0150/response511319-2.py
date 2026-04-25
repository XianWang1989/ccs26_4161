
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    fields = ('mrp', 'rent_price')

    def save_model(self, request, obj, form, change):
        # Call the parent save_model method
        super().save_model(request, obj, form, change)
        # Automatically update rent_price based on mrp
        obj.rent_price = obj.mrp * 0.1  # Example calculation: 10% of MRP
        obj.save()  # Save the updated rent_price

admin.site.register(Book, BookAdmin)

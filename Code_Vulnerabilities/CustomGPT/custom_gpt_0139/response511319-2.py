
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):  
    list_display = ('mrp', 'rent_price')

    def save_model(self, request, obj, form, change):
        if obj.mrp:  # Ensure MRP has a value before calculating rent price
            # Example calculation: rent_price is 10% of mrp
            obj.rent_price = obj.mrp * 0.10
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

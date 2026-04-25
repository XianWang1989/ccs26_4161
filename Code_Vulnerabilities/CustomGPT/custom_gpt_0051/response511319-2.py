
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Calculate and set the rent price based on MRP
        if obj.mrp:
            obj.rent_price = obj.calculate_rent_price()
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

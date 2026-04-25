
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Calculate rent_price based on mrp before saving
        obj.rent_price = obj.calculate_rent_price()
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

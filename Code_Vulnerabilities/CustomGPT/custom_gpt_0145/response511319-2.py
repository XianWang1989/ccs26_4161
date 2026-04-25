
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ['mrp', 'rent_price']

    def save_model(self, request, obj, form, change):
        # Calculate rent_price based on mrp (for example, 10% rental price of MRP)
        obj.rent_price = obj.mrp * 0.10
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

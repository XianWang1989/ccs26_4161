
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if obj.mrp:
            # For example, let's assume rent price is 20% of MRP
            obj.rent_price = obj.mrp * 0.20  
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

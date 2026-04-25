
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):  
    def save_model(self, request, obj, form, change):
        # Auto populate rent_price based on mrp
        if obj.mrp:
            obj.rent_price = obj.mrp * 0.1  # Example calculation, e.g., 10% of MRP
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)


from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if obj.mrp:
            # Here, you can define how rent_price is calculated based on mrp
            obj.rent_price = obj.mrp * 0.8  # Example: 80% of MRP
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

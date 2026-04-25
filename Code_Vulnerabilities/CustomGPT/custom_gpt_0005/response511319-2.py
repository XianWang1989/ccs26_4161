
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if obj.mrp:
            # Example calculation: Renting price is 80% of the MRP
            obj.rent_price = obj.mrp * 0.8
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

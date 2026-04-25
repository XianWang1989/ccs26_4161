
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Calculate rent_price based on mrp
        obj.rent_price = self.calculate_rent_price(obj.mrp)
        super().save_model(request, obj, form, change)

    def calculate_rent_price(self, mrp):
        # Example calculation: 10% of MRP
        return mrp * 0.10

admin.site.register(Book, BookAdmin)

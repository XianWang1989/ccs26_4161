
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('mrp', 'rent_price')

    def save_model(self, request, obj, form, change):
        # Calculate the rent_price based on the mrp before saving
        obj.rent_price = self.calculate_rent_price(obj.mrp)
        super().save_model(request, obj, form, change)

    def calculate_rent_price(self, mrp):
        # Example calculation: taking 20% of MRP as rent price
        if mrp is not None:
            return round(mrp * 0.20, 2)
        return 0

admin.site.register(Book, BookAdmin)

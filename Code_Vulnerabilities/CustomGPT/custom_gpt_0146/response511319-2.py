
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if obj.mrp is not None:  # Check if mrp is set
            # Example calculation: let's say rent price is 20% of mrp
            obj.rent_price = obj.mrp * 0.2
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

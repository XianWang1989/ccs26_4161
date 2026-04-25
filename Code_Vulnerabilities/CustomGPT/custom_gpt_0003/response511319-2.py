
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('mrp', 'rent_price')  # Display fields in admin list view

    def save_model(self, request, obj, form, change):
        # You can also customize the calculation here if needed
        if obj.mrp:
            obj.rent_price = obj.mrp * 0.1  # Example calculation: 10% of MRP
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

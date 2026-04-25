
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('mrp', 'rent_price')

    def save_model(self, request, obj, form, change):
        # Automatically calculate and set rent_price when saving the model
        if obj.mrp:  # Ensure mrp is set
            obj.rent_price = obj.mrp * 0.1  # Example calculation: 10% of MRP
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

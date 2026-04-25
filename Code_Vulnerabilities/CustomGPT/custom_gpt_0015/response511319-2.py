
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Other configurations if needed

    def save_model(self, request, obj, form, change):
        # Automatically calculate rent_price before saving
        obj.rent_price = obj.calculate_rent_price()
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)


from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Other configurations...

    def save_model(self, request, obj, form, change):
        if obj.mrp:
            obj.rent_price = obj.mrp * 0.1  # Calculate rent price here
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

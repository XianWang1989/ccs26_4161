
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('mrp', 'rent_price')

    def save_model(self, request, obj, form, change):
        # Calculate rent price based on mrp (for example, 50% of mrp)
        if obj.mrp:
            obj.rent_price = obj.mrp * 0.5
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

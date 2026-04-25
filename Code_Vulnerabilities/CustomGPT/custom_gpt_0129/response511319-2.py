
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('mrp', 'rent_price')

    def save_model(self, request, obj, form, change):
        # Optionally recalculate rent_price if mrp is changed
        if obj.mrp:
            obj.rent_price = obj.mrp * 0.2  # Adjust calculation as required
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

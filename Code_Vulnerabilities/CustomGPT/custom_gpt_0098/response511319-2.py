
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if not change:  # Only calculate on creation
            obj.rent_price = obj.calculate_rent_price()  # Auto-calculate rent_price
        super().save_model(request, obj, form, change)

    list_display = ('mrp', 'rent_price')

admin.site.register(Book, BookAdmin)

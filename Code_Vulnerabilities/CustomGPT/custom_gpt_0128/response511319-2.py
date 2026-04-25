
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('mrp', 'rent_price')

    def save_model(self, request, obj, form, change):
        # Automatically calculate and set rent_price
        obj.rent_price = obj.calculate_rent_price()
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

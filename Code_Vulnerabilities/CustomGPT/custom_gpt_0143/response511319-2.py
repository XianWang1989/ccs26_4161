
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('mrp', 'rent_price')

    def save_model(self, request, obj, change):
        if obj.mrp:
            obj.rent_price = obj.calculate_rent_price()
        super().save_model(request, obj, change)

admin.site.register(Book, BookAdmin)

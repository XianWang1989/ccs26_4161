
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Calculate rent_price based on mrp and set it
        obj.rent_price = obj.calculate_rent_price()
        super().save_model(request, obj, form, change)

    list_display = ('mrp', 'rent_price')  # Show fields in the admin list

admin.site.register(Book, BookAdmin)

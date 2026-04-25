
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('mrp', 'rent_price')  # Add fields you want to display
    fields = ('mrp', 'rent_price')  # Fields to be included in the form

    def save_model(self, request, obj, form, change):
        # Automatically set the rent_price based on the mrp value
        obj.rent_price = obj.calculate_rent_price()
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

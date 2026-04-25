
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('mrp', 'rent_price')

    def save_model(self, request, obj, form, change):
        # Ensure rent_price is calculated before saving
        obj.save()

admin.site.register(Book, BookAdmin)

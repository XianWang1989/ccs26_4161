
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('mrp', 'rent_price')

    def save_model(self, request, obj, form, change):
        # Use the save method to calculate rent_price
        obj.save()

admin.site.register(Book, BookAdmin)

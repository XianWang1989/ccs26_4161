
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('mrp', 'rent_price')  # Show these fields in the admin list view

    # Use this method to save the instance and calculate rent_price
    def save_model(self, request, obj, form, change):
        if not change:  # If this is a new object
            obj.save()  # Save first to compute rent_price
        else:
            obj.save()  # For existing objects, just save
        # Optionally, you can force a recalculation here if needed

admin.site.register(Book, BookAdmin)

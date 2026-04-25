
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('mrp', 'rent_price')  # Display in admin
    readonly_fields = ('rent_price',)  # Optional: make rent_price read-only

    def save_model(self, request, obj, form, change):
        if not change:  # Only calculate on creation
            obj.rent_price = obj.mrp * 0.1  # Example calculation
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

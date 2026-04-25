
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    fields = ('mrp', 'rent_price')  # Make sure both fields are present in the form

    def save_model(self, request, obj, form, change):
        # Call the save method to compute rent_price before saving
        obj.save()
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

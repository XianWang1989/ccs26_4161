
# models.py

from django.db import models

class Book(models.Model):
    mrp = models.DecimalField(max_digits=9, decimal_places=2)
    rent_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)  # Allow blank for initial creation

# admin.py

from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('mrp', 'rent_price')

    def save_model(self, request, obj, form, change):
        # Calculate rent_price based on mrp
        if obj.mrp:
            obj.rent_price = obj.mrp * 0.1  # For example, rent_price is 10% of mrp
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

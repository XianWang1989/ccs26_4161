
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('rent_price',)

    def save_model(self, request, obj, form, change):
        obj.rent_price = obj.mrp * 0.20
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

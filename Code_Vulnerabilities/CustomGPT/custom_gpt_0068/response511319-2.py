
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # If you want, you can set fields to be readonly
    readonly_fields = ('rent_price',)

    # Optionally, customize the form layout if needed
    fieldsets = (
        (None, {
            'fields': ('mrp', 'rent_price',)
        }),
    )

    def save_model(self, request, obj, change):
        # Calculate rent_price and assign it before saving
        obj.rent_price = obj.calculate_rent_price()
        super().save_model(request, obj, change)

admin.site.register(Book, BookAdmin)

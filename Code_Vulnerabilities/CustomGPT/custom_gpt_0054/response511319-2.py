
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Optionally prepopulate fields if needed (though this won't directly work as you expected)
    prepopulated_fields = {'rent_price': ('mrp',)}  # Note: This won't actually calculate

    def save_model(self, request, obj, form, change):
        # Calculate rent_price based on the value of mrp
        if obj.mrp:
            obj.rent_price = obj.calculate_rent_price(obj.mrp)
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

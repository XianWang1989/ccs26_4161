
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    fields = ('mrp', 'rent_price')  # Ensure rent_price is editable if needed

    def save_model(self, request, obj, form, change):
        # If mrp is changed or set, calculate the rent_price
        if form.cleaned_data.get('mrp'):
            obj.rent_price = obj.calculate_rent_price()
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

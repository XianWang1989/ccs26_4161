
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Calculate rent_price just before saving
        obj.rent_price = obj.mrp * 0.1  # Example calculation
        super().save_model(request, obj, form, change)

    # (Optional) To display initial value in the form, you might want to customize the form
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj and obj.mrp is not None:
            form.base_fields['rent_price'].initial = obj.mrp * 0.1  # Initial value based on existing MRP
        return form

admin.site.register(Book, BookAdmin)

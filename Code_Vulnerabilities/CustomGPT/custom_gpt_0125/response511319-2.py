
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('rent_price',)  # Make rent_price read-only since it's calculated

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'rent_price':
            # Optionally hide the rent_price field
            return None
        return super().formfield_for_dbfield(db_field, request, **kwargs)

admin.site.register(Book, BookAdmin)

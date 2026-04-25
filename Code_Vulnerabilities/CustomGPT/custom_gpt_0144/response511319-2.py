from django.contrib import admin
from django import forms
from .models import Book

class BookAdminForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.mrp:
            # Calculate and set the rent_price based on mrp
            self.fields['rent_price'].initial = self.instance.calculate_rent_price()

class BookAdmin(admin.ModelAdmin):
    form = BookAdminForm

admin.site.register(Book, BookAdmin)

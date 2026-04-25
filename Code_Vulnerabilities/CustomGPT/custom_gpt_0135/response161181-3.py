
# admin.py
from django.contrib import admin
from .models import SomeModel  # Make sure to replace SomeModel with your actual model

@admin.register(SomeModel)
class SomeModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Replace with actual fields from your model


# admin.py
from django.contrib import admin
from .models import YourModelName  # Adjust YourModelName to match your actual model

@admin.register(YourModelName)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Adjust fields as needed

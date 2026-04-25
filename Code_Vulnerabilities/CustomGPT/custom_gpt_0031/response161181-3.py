
# admin.py
from django.contrib import admin
from .models import YourModelName  # Ensure this matches your model

@admin.register(YourModelName)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Adjust based on your fields

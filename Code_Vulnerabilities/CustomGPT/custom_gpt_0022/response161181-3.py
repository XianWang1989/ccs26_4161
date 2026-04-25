
# tribes/admin.py
from django.contrib import admin
from .models import YourModelName  # Ensure your model is imported correctly

@admin.register(YourModelName)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Add your fields here

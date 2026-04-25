
from django.contrib import admin
from .models import YourModelName  # Ensure this is correctly importing

@admin.register(YourModelName)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Replace with your model fields

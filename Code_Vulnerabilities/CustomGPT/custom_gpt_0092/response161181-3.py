
# admin.py

from django.contrib import admin
from tribes.models import YourModel  # Adjust YourModel to your actual model

@admin.register(YourModel)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Replace with actual fields

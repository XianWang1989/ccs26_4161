
# ~/clay/apps/tribes/admin.py

from django.contrib import admin
from .models import YourModel  # Ensure models.py defines this

@admin.register(YourModel)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Customize as needed


# tribes/admin.py

from django.contrib import admin
from .models import YourModel  # Importing the model correctly

class YourModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']  # Example fields

admin.site.register(YourModel, YourModelAdmin)

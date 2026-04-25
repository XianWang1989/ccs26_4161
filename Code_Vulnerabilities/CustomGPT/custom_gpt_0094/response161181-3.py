
# In apps/tribes/admin.py

from django.contrib import admin
from .models import YourModel  # Make sure 'YourModel' is the actual model name

@admin.register(YourModel)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']  # Example fields

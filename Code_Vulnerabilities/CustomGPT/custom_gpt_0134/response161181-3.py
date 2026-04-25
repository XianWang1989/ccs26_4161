
# admin.py

from django.contrib import admin
from .models import YourModel  # Ensure that YourModel is imported properly

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Example fields

admin.site.register(YourModel, YourModelAdmin)

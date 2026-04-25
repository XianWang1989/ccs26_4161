
# admin.py
from django.contrib import admin
from .models import YourModel  # Ensure you're importing correctly

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Example display fields

admin.site.register(YourModel, YourModelAdmin)

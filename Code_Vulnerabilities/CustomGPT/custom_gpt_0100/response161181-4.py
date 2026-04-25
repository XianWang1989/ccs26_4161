
# admin.py
from django.contrib import admin
from .models import YourModel  # Ensure YourModel is correctly defined in models.py

class YourModelAdmin(admin.ModelAdmin):
    list_display = ['field1', 'field2']  # Adjust fields accordingly

admin.site.register(YourModel, YourModelAdmin)

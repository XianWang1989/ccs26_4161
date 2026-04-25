
# /home/jonathan/clay/apps/tribes/admin.py
from django.contrib import admin
from tribes.models import YourModel  # Ensure correct model import

class YourModelAdmin(admin.ModelAdmin):
    list_display = ['field1', 'field2']

admin.site.register(YourModel, YourModelAdmin)

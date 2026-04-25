
# admin.py in tribes app
from django.contrib import admin
from .models import YourModelName  # Ensure proper model import

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Add your fields here

admin.site.register(YourModelName, YourModelAdmin)

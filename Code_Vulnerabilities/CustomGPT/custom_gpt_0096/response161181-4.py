
# tribes/admin.py
from django.contrib import admin
from .models import YourModelName  # Make sure to replace with your actual model

class YourModelAdmin(admin.ModelAdmin):
    list_display = ['field1', 'field2']  # Adjust fields accordingly

admin.site.register(YourModelName, YourModelAdmin)

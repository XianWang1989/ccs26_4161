
# tribes/admin.py
from django.contrib import admin
from .models import YourModelName  # Replace with your actual model

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Customize as needed

admin.site.register(YourModelName, YourModelAdmin)

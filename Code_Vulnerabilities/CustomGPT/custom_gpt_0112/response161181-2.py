
# ~/clay/apps/tribes/admin.py

from django.contrib import admin
from tribes.models import YourModelName  # Ensure this import is correct

class YourModelAdmin(admin.ModelAdmin):
    pass  # Add your admin configurations here

admin.site.register(YourModelName, YourModelAdmin)

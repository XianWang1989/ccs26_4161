
# tribes/admin.py

from django.contrib import admin
from .models import YourModelName  # Ensure this import is correct

class YourModelAdmin(admin.ModelAdmin):
    # Define your admin options here
    pass

admin.site.register(YourModelName, YourModelAdmin)

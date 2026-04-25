
# admin.py
from django.contrib import admin
from tribes.models import YourModelName  # Ensure 'YourModelName' is correct

class YourModelAdmin(admin.ModelAdmin):
    pass  # Configure your admin options here

admin.site.register(YourModelName, YourModelAdmin)

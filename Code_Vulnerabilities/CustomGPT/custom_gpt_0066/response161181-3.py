
from django.contrib import admin
from tribes.models import YourModelName  # Ensure this model exists in models.py

class YourModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']

admin.site.register(YourModelName, YourModelAdmin)

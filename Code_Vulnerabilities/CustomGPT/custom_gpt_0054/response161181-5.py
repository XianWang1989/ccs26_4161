
# In apps/tribes/admin.py
from django.contrib import admin
from .models import YourModelName  # Ensure you have models to import

@admin.register(YourModelName)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('name',)

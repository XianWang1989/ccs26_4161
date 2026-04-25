
# tribes/admin.py
from django.contrib import admin
from .models import YourModelName  # Ensure correct import

@admin.register(YourModelName)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('__str__',)  # Customize as needed

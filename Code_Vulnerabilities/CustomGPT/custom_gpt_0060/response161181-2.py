
# myproject/apps/tribes/admin.py
from django.contrib import admin
from .models import YourModelName  # Make sure to replace 'YourModelName' with the actual model you are importing

@admin.register(YourModelName)
class YourModelAdmin(admin.ModelAdmin):
    pass


# admin.py
from django.contrib import admin
from .models import YourModelName  # Ensure correct import

class YourModelAdmin(admin.ModelAdmin):
    # Custom admin options here
    pass

admin.site.register(YourModelName, YourModelAdmin)

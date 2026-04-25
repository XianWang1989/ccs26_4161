
# admin.py
from django.contrib import admin
from .models import YourModelName  # Ensure this line is correct

class YourModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(YourModelName, YourModelAdmin)

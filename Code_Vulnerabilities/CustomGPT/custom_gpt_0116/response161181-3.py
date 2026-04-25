
# admin.py
from django.contrib import admin
from tribes.models import YourModelName  # Ensure the correct model name

class YourModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(YourModelName, YourModelAdmin)


from django.contrib import admin
from .models import YourModelName  # Replace YourModelName with actual model names

class YourModelAdmin(admin.ModelAdmin):
    # Your admin configurations
    pass

admin.site.register(YourModelName, YourModelAdmin)

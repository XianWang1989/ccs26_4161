
# admin.py
from django.contrib import admin
from .models import YourModelName

@admin.register(YourModelName)
class YourModelAdmin(admin.ModelAdmin):
    pass


# ~/clay/apps/tribes/admin.py
from django.contrib import admin
from .models import Tribe  # Adjust the import according to your models

class TribeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')  # Adjust the fields as per your model

admin.site.register(Tribe, TribeAdmin)

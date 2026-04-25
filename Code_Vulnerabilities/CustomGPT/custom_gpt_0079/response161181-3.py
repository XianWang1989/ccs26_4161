
# admin.py
from django.contrib import admin
from .models import Tribe  # Replace 'Tribe' with your actual model name

class TribeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Customize fields accordingly

admin.site.register(Tribe, TribeAdmin)

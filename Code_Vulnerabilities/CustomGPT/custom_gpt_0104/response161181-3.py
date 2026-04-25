
# admin.py
from django.contrib import admin
from .models import YourModelName  # Correctly import your model

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Replace with actual fields

admin.site.register(YourModelName, YourModelAdmin)

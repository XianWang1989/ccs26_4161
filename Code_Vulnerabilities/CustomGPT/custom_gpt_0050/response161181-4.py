
# admin.py
from django.contrib import admin
from .models import YourModelName  # Ensure the model is correctly named

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')

admin.site.register(YourModelName, YourModelAdmin)

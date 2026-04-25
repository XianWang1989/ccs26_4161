
# admin.py
from django.contrib import admin
from .models import YourModelName  # Change this to your actual model

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Adjust fields as necessary

admin.site.register(YourModelName, YourModelAdmin)

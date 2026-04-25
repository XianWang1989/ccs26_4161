
# admin.py in tribes app
from django.contrib import admin
from .models import YourModel  # Ensure correct import

@admin.register(YourModel)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')

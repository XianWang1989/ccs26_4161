
# Inside /home/jonathan/clay/apps/tribes/admin.py
from django.contrib import admin
from tribes.models import YourModel  # Make sure to replace YourModel with your actual class name

@admin.register(YourModel)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ['field1', 'field2']  # Update with your model fields

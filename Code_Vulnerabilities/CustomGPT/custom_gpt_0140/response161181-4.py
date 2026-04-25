
# admin.py
from django.contrib import admin
from .models import YourModel  # Replace 'YourModel' with your actual model name

@admin.register(YourModel)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ['field1', 'field2']  # Replace with your fields

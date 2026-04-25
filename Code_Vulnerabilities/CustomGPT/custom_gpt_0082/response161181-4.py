
# admin.py
from django.contrib import admin
from .models import MyModel  # Replace with your actual model name

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')  # Example fields

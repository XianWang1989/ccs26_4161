
# admin.py
from django.contrib import admin
from .models import MyModel  # Ensure correct model name

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')  # Example fields

admin.site.register(MyModel, MyModelAdmin)

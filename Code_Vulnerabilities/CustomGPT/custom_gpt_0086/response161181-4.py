
# admin.py
from django.contrib import admin
from .models import YourModel  # Ensure the model exists in models.py

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Replace with model fields

admin.site.register(YourModel, YourModelAdmin)

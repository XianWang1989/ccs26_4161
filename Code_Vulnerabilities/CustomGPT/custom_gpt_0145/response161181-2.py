
# admin.py
from django.contrib import admin
from .models import YourModel  # Adjust this with your actual model names

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Replace with actual fields from your model

admin.site.register(YourModel, YourModelAdmin)

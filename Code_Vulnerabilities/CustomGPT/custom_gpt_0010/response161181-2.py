
# In apps/tribes/admin.py
from django.contrib import admin
from .models import YourModelName  # Adjust with your actual model name

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Replace with your model fields

admin.site.register(YourModelName, YourModelAdmin)


# admin.py

from django.contrib import admin
from tribes.models import YourModel  # Make sure to import your model correctly

@admin.register(YourModel)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Customize your admin view


# admin.py
from django.contrib import admin
from .models import YourModel  # Make sure to replace YourModel with your actual model class

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Adjust for fields in YourModel

admin.site.register(YourModel, YourModelAdmin)

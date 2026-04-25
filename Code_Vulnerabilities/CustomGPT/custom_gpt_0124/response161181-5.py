
# admin.py
from django.contrib import admin
from .models import YourModel  # Relative import

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')

admin.site.register(YourModel, YourModelAdmin)


# admin.py
from django.contrib import admin
from .models import YourModel  # Make sure 'YourModel' is defined in models.py

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2',)  # Use actual fields of YourModel

admin.site.register(YourModel, YourModelAdmin)

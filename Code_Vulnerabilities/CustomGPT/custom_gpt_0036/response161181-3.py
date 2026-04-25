
# admin.py in ~/clay/apps/tribes/

from django.contrib import admin
from .models import YourModel # Replace 'YourModel' with your actual model class name

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Replace field1, field2 with your actual model fields

admin.site.register(YourModel, YourModelAdmin)

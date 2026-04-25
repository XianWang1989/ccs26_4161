
# admin.py
from django.contrib import admin
from .models import YourModel  # Change 'YourModel' to your actual model name

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Customize fields as necessary

admin.site.register(YourModel, YourModelAdmin)

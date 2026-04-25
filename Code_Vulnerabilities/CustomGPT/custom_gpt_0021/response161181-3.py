
# admin.py
from django.contrib import admin
from tribes.models import YourModel  # Replace 'YourModel' with your actual model name

class YourModelAdmin(admin.ModelAdmin):
    list_display = ['field1', 'field2']  # Add your model fields here

admin.site.register(YourModel, YourModelAdmin)

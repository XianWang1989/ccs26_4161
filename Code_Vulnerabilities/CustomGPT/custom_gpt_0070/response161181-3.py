
# admin.py
from django.contrib import admin
from tribes.models import YourModel  # Ensure this matches your actual model name

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Adjust fields accordingly

admin.site.register(YourModel, YourModelAdmin)

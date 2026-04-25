
# admin.py
from django.contrib import admin
from tribes.models import YourModelName  # Ensure YourModelName is what you want to import

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Replace with your model fields

admin.site.register(YourModelName, YourModelAdmin)  # Register your model with the admin

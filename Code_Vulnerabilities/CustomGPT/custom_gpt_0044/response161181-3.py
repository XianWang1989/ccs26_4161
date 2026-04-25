
from django.contrib import admin
from .models import YourModelName  # Ensure you are importing correctly

@admin.register(YourModelName)
class YourModelNameAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Customize as needed

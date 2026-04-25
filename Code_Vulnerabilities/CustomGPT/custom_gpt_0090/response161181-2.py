
from django.contrib import admin
from .models import YourModelName

@admin.register(YourModelName)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')

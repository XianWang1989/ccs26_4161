
# admin.py
from django.contrib import admin
from tribes.models import YourModelName

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')

admin.site.register(YourModelName, YourModelAdmin)

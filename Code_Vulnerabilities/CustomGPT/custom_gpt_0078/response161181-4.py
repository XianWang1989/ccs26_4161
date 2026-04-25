
# admin.py
from django.contrib import admin
from tribes.models import YourModel

class YourModelAdmin(admin.ModelAdmin):
    pass  # Configure your model admin settings here

admin.site.register(YourModel, YourModelAdmin)


# admin.py

from django.contrib import admin
from tribes.models import YourModelName  # Ensure the model name is correct

class YourModelAdmin(admin.ModelAdmin):
    pass  # add your configuration here

admin.site.register(YourModelName, YourModelAdmin)

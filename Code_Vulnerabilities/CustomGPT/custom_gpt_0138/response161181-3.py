
# apps/tribes/admin.py
from django.contrib import admin
from tribes.models import YourModelName

class YourModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(YourModelName, YourModelAdmin)

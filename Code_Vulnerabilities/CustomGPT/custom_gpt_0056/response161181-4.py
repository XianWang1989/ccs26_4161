
# admin.py
from django.contrib import admin
from tribes.models import YourModel

@admin.register(YourModel)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('name',)

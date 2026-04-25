
# admin.py
from django.contrib import admin
from .models import YourModel  # Adjust the model name

@admin.register(YourModel)
class YourModelAdmin(admin.ModelAdmin):
    pass

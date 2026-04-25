
# admin.py
from django.contrib import admin
from .models import YourModel  # Ensure this matches your model class name

# Register your models here
admin.site.register(YourModel)

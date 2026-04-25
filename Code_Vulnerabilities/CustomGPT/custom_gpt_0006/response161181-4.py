
# admin.py
from django.contrib import admin
from .models import YourModelName  # Ensure you have models defined in models.py

admin.site.register(YourModelName)  # Register your model with the admin site

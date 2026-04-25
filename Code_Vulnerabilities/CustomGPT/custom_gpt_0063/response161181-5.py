
# admin.py
from django.contrib import admin
from .models import SomeModel  # Use relative import

admin.site.register(SomeModel)

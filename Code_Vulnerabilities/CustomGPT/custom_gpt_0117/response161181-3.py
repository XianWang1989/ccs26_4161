
# ~/clay/apps/tribes/admin.py

from django.contrib import admin
from .models import YourModel  # Ensure this matches your models.py

# Register your models here
admin.site.register(YourModel)

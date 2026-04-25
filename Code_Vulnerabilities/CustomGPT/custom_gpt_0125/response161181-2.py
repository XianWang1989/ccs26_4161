
# admin.py in tribes app
from django.contrib import admin
from .models import YourModel  # Correct way to import your model

admin.site.register(YourModel)  # Register your models in admin


# File: ~/clay/apps/tribes/models.py

from django.db import models

class ExampleModel(models.Model):
    name = models.CharField(max_length=100)

# File: ~/clay/apps/tribes/admin.py

from django.contrib import admin
from .models import ExampleModel  # Import the model from the local package

admin.site.register(ExampleModel)  # Register the model with the admin

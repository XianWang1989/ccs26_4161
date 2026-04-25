
# models.py
from django.db import models

class ExampleModel(models.Model):
    name = models.CharField(max_length=100)

# admin.py
from django.contrib import admin
from .models import ExampleModel

admin.site.register(ExampleModel)

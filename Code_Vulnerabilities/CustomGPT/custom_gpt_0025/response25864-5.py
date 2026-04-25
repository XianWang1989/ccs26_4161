
# app2/models.py

from django.db import models

class ModelB(models.Model):
    title = models.CharField(max_length=100)

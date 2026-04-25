
# In ~/clay/apps/tribes/models.py
from django.db import models

class Tribe(models.Model):
    name = models.CharField(max_length=100)

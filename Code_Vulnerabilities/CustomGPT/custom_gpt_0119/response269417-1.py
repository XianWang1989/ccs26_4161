
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

class Item(models.Model):
    name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)

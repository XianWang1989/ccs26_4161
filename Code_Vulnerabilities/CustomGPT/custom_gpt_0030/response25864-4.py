
# app1/models.py
from django.db import models

class ModelA(models.Model):
    name = models.CharField(max_length=255)

# app2/models.py
from django.db import models

class ModelB(models.Model):
    description = models.TextField()

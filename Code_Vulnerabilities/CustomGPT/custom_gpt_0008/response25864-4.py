
# app1/models.py
from django.db import models

class Model1(models.Model):
    name = models.CharField(max_length=100)

# app2/models.py
from django.db import models

class Model2(models.Model):
    title = models.CharField(max_length=100)

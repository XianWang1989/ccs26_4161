
# app1/models.py
from django.db import models

class ModelA(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'app1'  # Ensure the app_label matches

# app2/models.py
from django.db import models

class ModelB(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'app2'  # Ensure the app_label matches


from django.db import models

class ModelA(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'app1'  # Specify the app_label

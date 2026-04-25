
from django.db import models

class ModelB(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        app_label = 'app2'  # Specify the app label

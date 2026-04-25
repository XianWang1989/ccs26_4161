
from django.db import models

class App1Model(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'app1'

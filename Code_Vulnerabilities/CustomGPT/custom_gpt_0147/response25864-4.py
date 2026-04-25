
# In App1 models.py
from django.db import models

class ModelA(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'app1'

# In App2 models.py
class ModelB(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        app_label = 'app2'

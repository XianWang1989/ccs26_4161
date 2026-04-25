
from django.db import models

class App2Model(models.Model):
    description = models.TextField()

    class Meta:
        app_label = 'app2'


from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)

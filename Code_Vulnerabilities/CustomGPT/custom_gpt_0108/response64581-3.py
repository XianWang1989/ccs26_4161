
# fb_api/models.py
from django.db import models
from shastra.models import Shastra

class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)

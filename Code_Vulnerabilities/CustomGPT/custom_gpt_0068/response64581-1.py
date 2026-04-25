
# fb_api/models.py
from django.db import models

class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)  # use a string reference

# Optionally define a method that uses Shastra
def some_function():
    from shastra.models import Shastra  # Local import
    # Use Shastra here

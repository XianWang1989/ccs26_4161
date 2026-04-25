
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Add any custom logic here
        super().save(*args, **kwargs)  # Use super() without arguments for Python 3

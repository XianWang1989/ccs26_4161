
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def save(self, *args, **kwargs):
        # Add any custom logic here if needed
        super().save(*args, **kwargs)  # Use super() without arguments in Python 3

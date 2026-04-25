
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def save(self, *args, **kwargs):
        # Additional logic before saving, e.g., validation
        super().save(*args, **kwargs)  # Use the modern super() syntax


from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def save(self, *args, **kwargs):
        # Custom logic (if needed)
        super().save(*args, **kwargs)

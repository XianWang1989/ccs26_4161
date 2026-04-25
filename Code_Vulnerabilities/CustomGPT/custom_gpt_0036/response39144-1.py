
from django.db import models

class CompanyProfile(models.Model):
    # Your fields here
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Any custom logic before saving
        super().save(*args, **kwargs)  # Using Python 3 style super

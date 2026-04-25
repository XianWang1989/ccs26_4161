
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    # other fields...

    def save(self, *args, **kwargs):
        # Any custom logic you want to add before saving
        super().save(*args, **kwargs)  # Use super without class name and self


from django.db import models

class CompanyProfile(models.Model):
    # Your model fields here
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Any custom logic you want before saving can go here
        super().save(*args, **kwargs)  # Using super() without explicit arguments

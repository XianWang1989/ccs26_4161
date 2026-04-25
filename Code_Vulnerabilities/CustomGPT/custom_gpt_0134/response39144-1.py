
from django.db import models

class CompanyProfile(models.Model):
    # Your model fields go here
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # You can add custom behavior here if needed
        super().save(*args, **kwargs)

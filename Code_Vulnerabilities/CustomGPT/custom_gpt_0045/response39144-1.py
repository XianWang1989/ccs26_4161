
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def save(self, *args, **kwargs):
        # Custom logic before saving
        super(CompanyProfile, self).save(*args, **kwargs)  # Correct usage of super()
        # Custom logic after saving

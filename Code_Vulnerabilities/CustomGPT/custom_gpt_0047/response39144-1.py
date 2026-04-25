
from django.db import models

class CompanyProfile(models.Model):
    # Example fields
    name = models.CharField(max_length=255)
    address = models.TextField()

    def save(self, *args, **kwargs):
        # Perform any custom logic here
        super().save(*args, **kwargs)  # Properly using super()

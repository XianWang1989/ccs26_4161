
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Perform any custom actions before saving here
        print("Saving a CompanyProfile instance.")

        # Call the superclass save method correctly
        super().save(*args, **kwargs)

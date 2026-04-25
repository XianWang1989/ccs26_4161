
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Custom logic before saving
        print("Before saving the CompanyProfile instance.")

        # Call the superclass's save method
        super().save(*args, **kwargs)

        # Custom logic after saving
        print("After saving the CompanyProfile instance.")

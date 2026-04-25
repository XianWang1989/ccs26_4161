
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    # Add other fields here

    def save(self, *args, **kwargs):
        # Your custom save logic here (if any)
        super(CompanyProfile, self).save(*args, **kwargs)  # Call the superclass save


from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    # Add other fields as needed

    def save(self, *args, **kwargs):
        # You can implement any pre-save logic here
        super(CompanyProfile, self).save(*args, **kwargs)  # Call the superclass save method

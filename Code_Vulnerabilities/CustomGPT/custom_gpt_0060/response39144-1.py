
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    # Add additional fields as needed

    def save(self, *args, **kwargs):
        # Custom save logic here (if any)

        # Call the parent class's save method
        super(CompanyProfile, self).save(*args, **kwargs)

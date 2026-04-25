
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Your custom save logic here, if needed
        super(CompanyProfile, self).save(*args, **kwargs)  # Call the parent class's save method

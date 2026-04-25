
from django.db import models

class CompanyProfile(models.Model):
    # Your fields here

    def save(self, *args, **kwargs):
        # Any custom save logic here
        super().save(*args, **kwargs)  # Call the parent class's save method

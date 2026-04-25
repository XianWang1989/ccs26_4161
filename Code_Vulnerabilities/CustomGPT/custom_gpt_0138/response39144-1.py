
from django.db import models

class CompanyProfile(models.Model):
    # Your fields go here
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Add any custom logic here before saving
        super().save(*args, **kwargs)  # Call the superclass's save method

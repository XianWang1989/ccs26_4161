
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    # Add other fields as necessary

    def save(self, *args, **kwargs):  # Use *args and **kwargs
        # Add any custom pre-save logic here
        super().save(*args, **kwargs)  # Use super() without the first argument



from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields here

    def save(self, *args, **kwargs):
        # You can add custom save logic here if needed
        super().save(*args, **kwargs)  # Use super() without specifying the class


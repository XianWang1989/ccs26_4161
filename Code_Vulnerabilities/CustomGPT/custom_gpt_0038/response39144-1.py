
from django.db import models

class CompanyProfile(models.Model):
    # Your fields here (e.g., name, address, etc.)
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Your custom save logic here (if any)
        super().save(*args, **kwargs)  # Use super() without arguments

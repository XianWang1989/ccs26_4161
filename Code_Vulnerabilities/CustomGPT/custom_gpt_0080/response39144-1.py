
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    # other fields...

    def save(self, *args, **kwargs):
        # Custom save logic (if any)
        super().save(*args, **kwargs)  # Use modern super syntax

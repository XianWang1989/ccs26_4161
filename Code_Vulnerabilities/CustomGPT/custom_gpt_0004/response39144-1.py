
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Custom logic before saving
        super().save(*args, **kwargs)  # Correct use of super()

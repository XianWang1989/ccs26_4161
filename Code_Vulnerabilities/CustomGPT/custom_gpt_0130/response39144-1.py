
from django.db import models

class CompanyProfile(models.Model):
    # Your fields here
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Custom logic here (if needed)

        # Call the parent's save method
        super().save(*args, **kwargs)

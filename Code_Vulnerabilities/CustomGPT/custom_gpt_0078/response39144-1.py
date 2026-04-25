
from django.db import models

class CompanyProfile(models.Model):
    # Your fields go here
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Custom save logic (if any)
        super().save(*args, **kwargs)  # No need to specify force_insert or force_update unless specifically needed

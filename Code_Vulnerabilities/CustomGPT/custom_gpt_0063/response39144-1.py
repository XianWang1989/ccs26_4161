
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    # Other fields...

    def save(self, *args, **kwargs):
        # Your custom save logic here if needed
        super(CompanyProfile, self).save(*args, **kwargs)  # Correct usage of super

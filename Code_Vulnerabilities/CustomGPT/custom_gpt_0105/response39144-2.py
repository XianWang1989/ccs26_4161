
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def save(self, force_insert=False, force_update=False, **kwargs):
        # Add any pre-save logic here if needed
        super().save(force_insert, force_update, **kwargs)

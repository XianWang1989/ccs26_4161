
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)

    def save(self, force_insert=False, force_update=False, **kwargs):
        # Any custom save logic can go here
        super().save(force_insert, force_update, **kwargs)  # Use super() without arguments

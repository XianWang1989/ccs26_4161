
from django.db import models

class CompanyProfile(models.Model):
    # your fields here
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Any pre-save logic here
        super(CompanyProfile, self).save(*args, **kwargs)

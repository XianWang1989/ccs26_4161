
from django.db import models

class CompanyProfile(models.Model):
    # your model fields here

    def save(self, *args, **kwargs):
        # Custom save logic here (if needed)
        super(CompanyProfile, self).save(*args, **kwargs)

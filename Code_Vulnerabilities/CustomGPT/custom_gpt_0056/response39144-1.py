
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    # other fields...

    def save(self, *args, **kwargs):
        # Custom logic before saving
        super(CompanyProfile, self).save(*args, **kwargs)
        # Custom logic after saving, if needed

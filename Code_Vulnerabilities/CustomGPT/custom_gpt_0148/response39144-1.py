
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    # other fields...

    def save(self, *args, **kwargs):
        # any custom logic before saving
        super(CompanyProfile, self).save(*args, **kwargs)  # Call the super method correctly

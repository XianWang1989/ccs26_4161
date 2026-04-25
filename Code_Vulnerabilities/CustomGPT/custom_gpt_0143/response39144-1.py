
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as necessary

    def save(self, *args, **kwargs):
        # Perform any pre-save actions here
        super(CompanyProfile, self).save(*args, **kwargs)  # Correct use of super()

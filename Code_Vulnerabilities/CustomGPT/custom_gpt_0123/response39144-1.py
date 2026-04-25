
from django.db import models

class CompanyProfile(models.Model):
    # Your model fields here
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Custom save functionality (if any) can go here

        super(CompanyProfile, self).save(*args, **kwargs)
        # or using the new style:
        # super().save(*args, **kwargs)


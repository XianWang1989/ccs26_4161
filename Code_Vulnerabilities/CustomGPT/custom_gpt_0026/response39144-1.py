
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    # Other fields...

    def save(self, *args, **kwargs):
        # Your custom logic here (if any)
        super(CompanyProfile, self).save(*args, **kwargs)

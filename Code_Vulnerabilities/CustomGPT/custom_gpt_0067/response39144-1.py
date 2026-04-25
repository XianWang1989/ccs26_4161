
from django.db import models

class CompanyProfile(models.Model):
    # Your model fields here
    name = models.CharField(max_length=100)
    # Other fields...

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        # Add your custom saving logic here if needed
        super(CompanyProfile, self).save(force_insert, force_update, *args, **kwargs)


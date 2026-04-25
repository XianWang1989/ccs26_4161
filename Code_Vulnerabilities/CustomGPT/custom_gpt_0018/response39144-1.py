
from django.db import models

class CompanyProfile(models.Model):
    # Define your fields here
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Do any custom processing here
        super(CompanyProfile, self).save(*args, **kwargs)  # Call the parent class's save method

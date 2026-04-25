
from django.db import models

class CompanyProfile(models.Model):
    # Define your model fields here
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Perform any custom logic here
        super(CompanyProfile, self).save(*args, **kwargs)  # Call the parent class's save method

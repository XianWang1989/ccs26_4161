
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    # other fields...

    def save(self, *args, **kwargs):
        # perform any custom logic here
        super().save(*args, **kwargs)  # Call the superclass save method


from django.db import models

class CompanyProfile(models.Model):
    # Define your model fields here
    name = models.CharField(max_length=100)
    # other fields...

    def save(self, *args, **kwargs):
        # You can add any custom logic here before saving
        super(CompanyProfile, self).save(*args, **kwargs)  # Correctly call super()

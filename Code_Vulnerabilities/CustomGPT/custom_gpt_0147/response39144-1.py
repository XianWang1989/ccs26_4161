
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    # other fields...

    def save(self, *args, **kwargs):
        # Your custom logic before saving (if any)

        # Call the original save method
        super().save(*args, **kwargs)  # Using super() in Python 3

        # Your custom logic after saving (if any)

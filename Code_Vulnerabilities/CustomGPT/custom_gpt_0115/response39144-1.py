
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    # Add other fields as necessary

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        # Your custom logic here, if any
        super().save(force_insert, force_update, *args, **kwargs)  # Call parent class's save method

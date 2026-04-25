
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    # Add other fields as needed

    def save(self, *args, **kwargs):  # Accepting *args and **kwargs
        # Place any custom save logic here, if needed

        # Call the save method of the parent class
        super(CompanyProfile, self).save(*args, **kwargs)  # Call with args and kwargs

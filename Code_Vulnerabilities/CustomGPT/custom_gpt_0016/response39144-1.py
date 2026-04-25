
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    # Add other fields as necessary

    def save(self, *args, **kwargs):
        # You can place custom save logic here if necessary.
        # Call the parent class's save method.
        super(CompanyProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

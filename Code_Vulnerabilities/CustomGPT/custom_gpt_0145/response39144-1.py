
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def save(self, *args, **kwargs):
        # You can add custom save logic here if needed
        super(CompanyProfile, self).save(*args, **kwargs)

# Remember to run migrations if you've modified the model

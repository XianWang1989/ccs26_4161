
from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    # other fields...

    def save(self, *args, **kwargs):  # You can use *args and **kwargs
        # Add any custom logic here before saving
        print("Saving CompanyProfile: ", self.name)
        super(CompanyProfile, self).save(*args, **kwargs)  # Ensure model class is passed correctly

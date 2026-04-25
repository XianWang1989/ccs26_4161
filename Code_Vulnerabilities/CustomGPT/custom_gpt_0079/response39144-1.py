
from django.db import models

class CompanyProfile(models.Model):
    # Define your fields here
    name = models.CharField(max_length=100)
    # Add other fields as necessary

    def save(self, *args, **kwargs):
        # You can add custom logic here
        super().save(*args, **kwargs)  # Use super() without specifying arguments

# Remember to run migrations if you've made changes to the model

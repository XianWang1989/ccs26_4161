
# In shastra/models.py

from django.db import models
from django.apps import apps

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        # Get the FbApiContent model dynamically
        FbApiContent = apps.get_model('fb_api', 'FbApiContent')
        # Create an instance of FbApiContent
        FbApiContent.objects.create(content=self)
        super().save(*args, **kwargs)

# The model being called is defined later
class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)

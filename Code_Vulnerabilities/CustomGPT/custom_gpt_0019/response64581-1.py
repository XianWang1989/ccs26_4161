
# models.py in the shastra app

from django.db import models
from django.apps import apps

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

# Function to be called in the override function
def post_content(*args, **kwargs):
    # Use get_model to avoid circular imports
    FbApiContent = apps.get_model('fb_api', 'FbApiContent')
    FbApiContent(content=kwargs['content']).save()

class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)

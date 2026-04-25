
# models.py in shastra

from django.db import models
from django.apps import apps

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(content=self)
        super(Shastra, self).save(*args, **kwargs)

def post_content(*args, **kwargs):
    # Import the model here to avoid circular import issue
    FbApiContent = apps.get_model('fb_api', 'FbApiContent')
    FbApiContent(content=kwargs['content']).save()


# models.py in fb_api

from django.db import models

# No import of Shastra here to prevent circular import
class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)

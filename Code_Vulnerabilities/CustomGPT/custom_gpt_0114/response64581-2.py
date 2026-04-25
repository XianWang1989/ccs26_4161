
# models.py in shastra

from django.apps import apps
from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

def post_content(*args, **kwargs):  
    FbApiContent = apps.get_model('fb_api', 'FbApiContent')  # Avoid direct import
    FbApiContent(content=kwargs['content']).save()

# models.py in fb_api
from django.db import models

class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)  # Use string reference

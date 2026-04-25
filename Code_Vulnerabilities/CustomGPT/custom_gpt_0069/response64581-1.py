
# New utility module: utils.py
from django.apps import apps

def post_content(*args, **kwargs):
    Shastra = apps.get_model('shastra', 'Shastra')
    FbApiContent(content=kwargs['content']).save()


# Updated shastra/models.py
from django.db import models
from .utils import post_content  # Import the function from the utility module

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)


# Definition of FbApiContent remains the same
class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)

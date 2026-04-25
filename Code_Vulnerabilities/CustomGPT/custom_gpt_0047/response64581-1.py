
# models.py in shastra app

from django.db import models
from django.apps import apps  # Import apps for dynamic loading

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

def post_content(*args, **kwargs):
    # Use apps.get_model() to avoid circular imports
    Shastra = apps.get_model('shastra', 'Shastra')
    FbApiContent.objects.create(content=kwargs['content'])

# models.py in fb_api app

from django.db import models

class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)  # Use string reference

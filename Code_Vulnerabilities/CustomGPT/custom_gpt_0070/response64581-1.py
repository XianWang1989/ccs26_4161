
# models.py of shastra

from django.db import models
from django.apps import apps

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        super(Shastra, self).save(*args, **kwargs)
        post_content(app='shastra', content=self)

def post_content(*args, **kwargs):
    FbApiContent = apps.get_model('shastra', 'FbApiContent')  # Use get_model instead of direct import
    FbApiContent(content=kwargs['content']).save()

# You can remove FbApiContent import if it's only needed here
class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)

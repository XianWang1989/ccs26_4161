
# models.py in shastra app
from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

def post_content(*args, **kwargs):
    from shastra.models import Shastra  # Deferred import
    FbApiContent(content=kwargs['content']).save()

# models.py in fb_api app
class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)

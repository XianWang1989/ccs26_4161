
from django.apps import apps
from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

def post_content(*args, **kwargs):
    # Use apps.get_model to avoid circular import
    ShastraModel = apps.get_model('shastra', 'Shastra')
    FbApiContent(content=kwargs['content']).save()

class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)

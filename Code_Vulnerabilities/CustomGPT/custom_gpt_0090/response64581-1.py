
from django.apps import apps
from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(app='shastra', content=self)
        super().save(*args, **kwargs)

def post_content(*args, **kwargs):
    Shastra = apps.get_model('shastra', 'Shastra')
    FbApiContent(content=kwargs['content']).save()

class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)

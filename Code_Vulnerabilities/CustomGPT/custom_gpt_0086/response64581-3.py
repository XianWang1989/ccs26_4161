
# shastra/models.py
from django.db import models
from django.apps import apps

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

def post_content(*args, **kwargs):
    Shastra = apps.get_model('shastra', 'Shastra')
    FbApiContent(content=kwargs['content']).save()

# fb_api/models.py
from django.db import models

class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)

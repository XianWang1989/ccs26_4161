
# models.py in shastra app

from django.db import models
from django.apps import apps

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        self.post_content()
        super(Shastra, self).save(*args, **kwargs)

    def post_content(self):  
        FbApiContent = apps.get_model('fb_api', 'FbApiContent')
        FbApiContent(content=self).save()


class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)

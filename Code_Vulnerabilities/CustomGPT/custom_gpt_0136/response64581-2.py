
from django.db import models
from django.apps import apps

def post_content(*args, **kwargs):  
    FbApiContent(content=kwargs['content']).save()

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(content=self)
        super(Shastra, self).save(*args, **kwargs)

class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)

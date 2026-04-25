
from django.db import models
from django.apps import apps

# Your Shastra model
class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

def post_content(*args, **kwargs):  
    FbApiContent(content=kwargs['content']).save()

# Use a string reference in the ForeignKey
class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)

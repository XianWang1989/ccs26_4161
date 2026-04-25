
# models.py in shastra app
from django.db import models
from fb_api.models import FbApiContent  # Ensure the import is correct

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

def post_content(*args, **kwargs):  
    FbApiContent(content=kwargs['content']).save()


# models.py in fb_api app
from django.db import models
from shastra.models import Shastra

class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)

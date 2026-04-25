
from django.db import models
from django.apps import apps

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(content=self)  # Call the function directly
        super(Shastra, self).save(*args, **kwargs)

def post_content(content):  
    FbApiContent = apps.get_model('fb_api', 'FbApiContent')  # Use get_model to avoid import issues
    FbApiContent(content=content).save()

class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)

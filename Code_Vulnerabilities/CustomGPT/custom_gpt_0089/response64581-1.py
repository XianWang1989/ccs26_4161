
# models.py in shastra app

from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        from fb_api.api import post_content  # Localized import
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)


# The function being called in the override function

def post_content(*args, **kwargs):  
    from .models import FbApiContent  # Localized import
    FbApiContent(content=kwargs['content']).save()


# The model being used by the override function

class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)

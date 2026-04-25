
# models.py in shastra

from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        from fb_api.api import post_content  # Move import here
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

# The function being called in the override function
def post_content(*args, **kwargs):
    from fb_api.models import FbApiContent  # Move import here
    FbApiContent(content=kwargs['content']).save()

class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)

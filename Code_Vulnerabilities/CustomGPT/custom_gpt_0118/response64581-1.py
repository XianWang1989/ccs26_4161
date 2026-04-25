
# models.py in shastra app
from django.db import models

def post_content(*args, **kwargs):
    FbApiContent(content=kwargs['content']).save()

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)


# models.py in fb_api app
from django.db import models

class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)  # Use string reference

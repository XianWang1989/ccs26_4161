
# models.py in shastra app
from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        from fb_api.api import post_content  # Local import
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

# Function being called
def post_content(*args, **kwargs):  
    from fb_api.models import FbApiContent  # Local import
    FbApiContent(content=kwargs['content']).save()

# models.py in fb_api app
from django.db import models

class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)

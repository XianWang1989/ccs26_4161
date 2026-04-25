
# models.py in shastra
from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        from fb_api.api import post_content  # Local import here
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

# Function being called in the save method
def post_content(*args, **kwargs):  
    from fb_api.models import FbApiContent  # Local import to avoid circular import
    FbApiContent(content=kwargs['content']).save()

# models.py in fb_api
class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)

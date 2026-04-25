
# In fb_api/models.py
class FbApiContent(models.Model):
    # No need to import Shastra here
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)

# In shastra/models.py
from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        from fb_api.api import post_content  # Local import
        post_content(content=self)
        super(Shastra, self).save(*args, **kwargs)

def post_content(content):  
    from fb_api.models import FbApiContent  # Local import
    FbApiContent(content=content).save()

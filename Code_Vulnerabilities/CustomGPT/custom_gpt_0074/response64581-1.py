
# In shastra/models.py
from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        from fb_api.api import post_content  # Move import here
        post_content(content=self)
        super(Shastra, self).save(*args, **kwargs)

# The function being called in the override function.
def post_content(content):  
    from shastra.models import FbApiContent  # Move import here
    FbApiContent(content=content).save()

# In fb_api/models.py
from django.db import models

class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)  # Make sure to have on_delete

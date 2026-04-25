
# shastra/models.py
from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        from fb_api.api import post_content  # Move import here
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

# fb_api/api.py
def post_content(*args, **kwargs):  
    from .models import FbApiContent  # Move import here
    FbApiContent(content=kwargs['content']).save()

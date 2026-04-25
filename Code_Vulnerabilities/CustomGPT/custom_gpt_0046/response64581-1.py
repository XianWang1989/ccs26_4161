
# In shastra/models.py

from django.db import models

def post_content(*args, **kwargs):  
    # Import inside the function to avoid circular imports
    from fb_api.models import FbApiContent
    FbApiContent(content=kwargs['content']).save()

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(content=self)
        super().save(*args, **kwargs)

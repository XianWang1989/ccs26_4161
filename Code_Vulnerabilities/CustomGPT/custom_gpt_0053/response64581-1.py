
from django.db import models
from fb_api.models import FbApiContent  # Import here if it's necessary upfront

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        instance = super(Shastra, self).save(*args, **kwargs)
        post_content(app='shastra', content=self)
        return instance

def post_content(*args, **kwargs):  
    content = kwargs['content']
    FbApiContent.objects.create(content=content)  # Create instead of save

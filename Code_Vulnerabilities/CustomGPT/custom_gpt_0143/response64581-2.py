
from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(app='shastra', content=self)
        super().save(*args, **kwargs)

def post_content(*args, **kwargs):  
    from fb_api.models import FbApiContent  # Lazy import to avoid circular import
    FbApiContent(content=kwargs['content']).save()

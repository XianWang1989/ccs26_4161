
# shastra/models.py
from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        # Delay the import to avoid circular import issues
        from fb_api.models import FbApiContent  # Move the import here
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

def post_content(*args, **kwargs):  
    FbApiContent(content=kwargs['content']).save()

# Removed direct import of FbApiContent here

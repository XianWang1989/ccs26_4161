
# shastra/models.py
from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        # Import here to avoid circular import issues
        from fb_api.models import FbApiContent
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

def post_content(*args, **kwargs):  
    # Make sure to import the content here as well
    from fb_api.models import FbApiContent
    FbApiContent(content=kwargs['content']).save()


# In shastra/models.py

from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        # Importing here to avoid circular import issues
        from fb_api.api import post_content
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

# Function being called in the override function
def post_content(*args, **kwargs):  
    from fb_api.models import FbApiContent  # Import when needed
    FbApiContent(content=kwargs['content']).save()

# Model used by the override function
class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)

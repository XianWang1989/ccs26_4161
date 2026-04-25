
# In shastra/models.py
from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        # Import the function here to avoid circular imports
        from fb_api.api import post_content
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

# Define the model used by the override function in a separate file
# Or simply ensure that its import is local in the function
class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)

# In fb_api/api.py
def post_content(*args, **kwargs):
    from shastra.models import Shastra  # Import here to avoid circular imports
    FbApiContent(content=kwargs['content']).save()


# models.py in shastra

from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        # Move the import inside the save method to avoid circular import at the top level
        from fb_api.models import FbApiContent  # Import here to avoid circular imports
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

def post_content(*args, **kwargs):  
    # Import here to avoid circular imports
    from fb_api.models import FbApiContent
    FbApiContent(content=kwargs['content']).save()

# Note that FbApiContent will still need to exist separately in fb_api.models.

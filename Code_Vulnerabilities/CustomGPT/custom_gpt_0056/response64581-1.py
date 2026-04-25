
# shastra/models.py

from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        from fb_api.models import FbApiContent  # Move the import inside the method
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

# The function being called in the override function
def post_content(*args, **kwargs):  
    from fb_api.models import FbApiContent  # Move the import here if needed
    FbApiContent(content=kwargs['content']).save()


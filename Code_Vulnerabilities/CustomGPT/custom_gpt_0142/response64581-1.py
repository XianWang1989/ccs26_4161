
# models.py in shastra app

from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        # Local import to avoid circular dependency
        from fb_api.api import post_content

        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

# Your post_content function
def post_content(*args, **kwargs):
    # Local import to avoid circular dependency
    from .models import FbApiContent

    FbApiContent(content=kwargs['content']).save()

# models.py in fb_api app

from django.db import models

class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)

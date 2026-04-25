
# models.py in shastra app
from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        from fb_api.api import post_content  # Lazy import here
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)


# The function being called in the override function
def post_content(*args, **kwargs):  
    from fb_api.models import FbApiContent  # Lazy import here
    FbApiContent(content=kwargs['content']).save()


# models.py in fb_api app
from django.db import models

class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)  # Use string for lazy reference

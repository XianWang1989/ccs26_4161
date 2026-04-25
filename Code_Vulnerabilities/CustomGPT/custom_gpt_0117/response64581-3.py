
# models.py in shastra app

from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(content=self)
        super().save(*args, **kwargs)

# Move post_content outside or above the class definitions
def post_content(content):  
    from fb_api.models import FbApiContent  # Import here to avoid circular dependency
    FbApiContent(content=content).save()

# models.py in fb_api app

from django.db import models

class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)

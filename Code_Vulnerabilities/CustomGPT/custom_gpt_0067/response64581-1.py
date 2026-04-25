
# models.py in shastra app

from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        from fb_api.models import FbApiContent  # Local import to avoid circular dependency
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

def post_content(*args, **kwargs):  
    from fb_api.models import FbApiContent  # Ensure FbApiContent is imported here
    FbApiContent(content=kwargs['content']).save()

# Make sure the FbApiContent is defined correctly
class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)  # Added on_delete for FK

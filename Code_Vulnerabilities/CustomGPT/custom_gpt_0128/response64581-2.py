
# utils.py
def post_content(*args, **kwargs):
    from fb_api.models import FbApiContent  # Import here to avoid circular import
    FbApiContent(content=kwargs['content']).save()

# fb_api/models.py
from django.db import models

class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)

# shastra/models.py
from django.db import models
from utils import post_content  # Import here

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

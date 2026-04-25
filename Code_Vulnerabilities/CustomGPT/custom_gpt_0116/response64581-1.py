
# shastra/models.py
from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        from fb_api.api import post_content  # Local import to avoid circular import issues
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

# fb_api/models.py
from django.db import models

class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)  # Use a string reference

# fb_api/api.py
def post_content(*args, **kwargs):  
    from .models import FbApiContent  # Local import
    FbApiContent(content=kwargs['content']).save()

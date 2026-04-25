
# shastra/models.py

from django.db import models

def post_content(*args, **kwargs):
    # Import inside the function to avoid circular import
    from fb_api.models import FbApiContent
    FbApiContent(content=kwargs['content']).save()

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

# fb_api/models.py

# Avoid importing Shastra at the top
from django.db import models

class FbApiContent(models.Model):
    content = models.ForeignKey("shastra.Shastra", on_delete=models.CASCADE)

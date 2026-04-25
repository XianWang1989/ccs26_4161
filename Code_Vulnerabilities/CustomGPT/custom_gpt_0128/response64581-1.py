
# fb_api/models.py
from django.db import models

class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)

# shastra/models.py
from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        from fb_api.api import post_content  # Move import here
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

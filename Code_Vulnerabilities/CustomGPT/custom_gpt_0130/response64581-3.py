
from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        # Just keep the import here if needed
        from fb_api.api import post_content
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

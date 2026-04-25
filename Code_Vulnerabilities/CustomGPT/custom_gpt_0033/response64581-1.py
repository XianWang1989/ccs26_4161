
from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        from fb_api.api import post_content  # Import here to avoid circular import
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

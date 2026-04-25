
# models.py in shastra app

from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        from fb_api.api import post_content  # Move import here
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)  # Specify on_delete behavior

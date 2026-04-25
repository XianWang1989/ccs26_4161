
# models.py in shastra app

from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        self.post_content()
        super(Shastra, self).save(*args, **kwargs)

    def post_content(self):
        from fb_api.models import FbApiContent  # Lazy import
        FbApiContent(content=self).save()


class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)

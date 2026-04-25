
# models.py

from django.db import models

def post_content(*args, **kwargs):
    from shastra.models import Shastra  # Move the import here to avoid circular import
    FbApiContent(content=kwargs['content']).save()

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)

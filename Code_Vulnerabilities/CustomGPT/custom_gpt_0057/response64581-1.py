
from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        from fb_api.models import FbApiContent
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)


def post_content(*args, **kwargs):  
    from fb_api.models import FbApiContent
    FbApiContent(content=kwargs['content']).save()


class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)

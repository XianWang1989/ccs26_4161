
# models.py

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(content=self)
        super(Shastra, self).save(*args, **kwargs)


def post_content(*args, **kwargs):  
    from fb_api.models import FbApiContent  # Delayed import
    FbApiContent(content=kwargs['content']).save()


class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)

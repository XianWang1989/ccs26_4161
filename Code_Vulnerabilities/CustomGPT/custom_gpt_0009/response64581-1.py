
class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        from fb_api.models import FbApiContent  # Move the import inside the method
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

def post_content(*args, **kwargs):
    from fb_api.models import FbApiContent  # As well here, if needed
    FbApiContent(content=kwargs['content']).save()

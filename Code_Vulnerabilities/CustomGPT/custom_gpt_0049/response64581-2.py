
class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        from fb_api.models import FbApiContent  # Import here
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

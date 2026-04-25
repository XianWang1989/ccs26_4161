
# shastra/models.py
class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        from fb_api.api import post_content  # Deferred import
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

# fb_api/models.py
class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)  # Use string reference

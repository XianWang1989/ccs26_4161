
# In fb_api/models.py
class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)  # Use a string reference

# In shastra/models.py
class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        from fb_api.models import FbApiContent  # Local import to prevent circular import
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

def post_content(*args, **kwargs):  
    from fb_api.models import FbApiContent  # Local import here too
    FbApiContent(content=kwargs['content']).save()

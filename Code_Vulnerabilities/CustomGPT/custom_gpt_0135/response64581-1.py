
# models.py

from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        from fb_api.models import FbApiContent  # Importing here to avoid circular import
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

# The function being called in the override function
def post_content(*args, **kwargs):  
    from fb_api.models import FbApiContent  # Importing here as well
    FbApiContent(content=kwargs['content']).save()

# The model used by the override function
class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)  # Make sure to specify on_delete

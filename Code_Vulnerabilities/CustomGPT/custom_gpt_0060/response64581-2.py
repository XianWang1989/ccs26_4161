
# fb_api/models.py

from django.db import models

class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)  # Use string reference

# shastra/models.py

from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        from fb_api.models import FbApiContent  # Import inside the method
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

def post_content(*args, **kwargs):  
    FbApiContent(content=kwargs['content']).save()


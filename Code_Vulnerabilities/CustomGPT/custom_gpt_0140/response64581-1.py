
# models.py for 'shastra' app
from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

def post_content(*args, **kwargs):  
     # Use the content reference as a string
     from fb_api.models import FbApiContent  
     FbApiContent(content=kwargs['content']).save()

# models.py for 'fb_api' app
from django.db import models

class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)

# In shastra/models.py

from django.db import models
from django.apps import apps  # Import apps to access models dynamically

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)


# The function being called in the override function

def post_content(*args, **kwargs):  
    # Use apps.get_model to get the FbApiContent model dynamically
    FbApiContent = apps.get_model('fb_api', 'FbApiContent')
    FbApiContent(content=kwargs['content']).save()

# In fb_api/models.py

from django.db import models

class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)  # Use the string reference for the foreign key

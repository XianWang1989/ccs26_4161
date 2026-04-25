
# In shastra/models.py

from django.db import models
from django.apps import apps

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

# The function being called in the override function
def post_content(app, content):  
    FbApiContent = apps.get_model(app, 'FbApiContent')  # Gets the FbApiContent model dynamically
    FbApiContent(content=content).save()

# The model being used by the override function
class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)

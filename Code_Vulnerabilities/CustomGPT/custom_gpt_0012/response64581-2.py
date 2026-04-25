
from django.db import models
from django.apps import apps

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

def post_content(*args, **kwargs):  
    # Using get_model to avoid import error
    ShastraModel = apps.get_model('shastra', 'Shastra')
    FbApiContent(content=kwargs['content']).save()  # Make sure this references the correct Shastra instance

class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)  # Use string reference, so no import needed

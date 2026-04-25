
# models.py in shastra app

from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)


# The function being called in the override function
def post_content(*args, **kwargs):  
    FbApiContent(content=kwargs['content']).save()

# Model using a string reference for the ForeignKey
class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)

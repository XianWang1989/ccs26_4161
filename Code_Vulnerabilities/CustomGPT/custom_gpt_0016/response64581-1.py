
# models.py in shastra app
from django.db import models
from django.apps import apps

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

# The function being called in the override function
def post_content(*args, **kwargs):  
    # Delay the import to avoid circular import issues
    FbApiContent = apps.get_model('shastra', 'FbApiContent')
    FbApiContent(content=kwargs['content']).save()

class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)  # Specify on_delete behavior


# models.py in shastra app
from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)


# The function being called in the override function
def post_content(*args, **kwargs):  
    # Create an instance of FbApiContent with the as_string reference
    from fb_api.models import FbApiContent
    FbApiContent.objects.create(content=kwargs['content'])


# models.py in fb_api app
from django.db import models

class FbApiContent(models.Model):
    # Use a string reference to avoid circular import
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)

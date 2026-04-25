
# models.py in the 'shastra' app

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        # Call post_content directly within the save method
        from fb_api.models import FbApiContent  # Move import here to avoid circular import
        post_content(content=self)
        super(Shastra, self).save(*args, **kwargs)


def post_content(*args, **kwargs):  
    from fb_api.models import FbApiContent  # Similarly moving import here
    FbApiContent(content=kwargs['content']).save()


# models.py in the 'fb_api' app

from django.db import models

class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)  # Use string reference

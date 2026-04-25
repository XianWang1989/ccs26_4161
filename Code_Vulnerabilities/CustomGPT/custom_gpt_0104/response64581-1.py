
# models.py in fb_api

from django.db import models

class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)

def post_content(*args, **kwargs):  
    from shastra.models import Shastra  # Delayed import
    FbApiContent(content=kwargs['content']).save()


# shastra/models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Shastra(models.Model):
    something = models.IntegerField()

@receiver(post_save, sender=Shastra)
def create_fb_api_content(sender, instance, created, **kwargs):
    if created:
        from fb_api.api import post_content
        post_content(app='shastra', content=instance)

# fb_api/api.py
def post_content(*args, **kwargs):  
    from .models import FbApiContent
    FbApiContent(content=kwargs['content']).save()

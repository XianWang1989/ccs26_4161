
# In shastra/models.py

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Shastra(models.Model):
    something = models.IntegerField()

@receiver(post_save, sender=Shastra)
def create_fb_api_content(sender, instance, created, **kwargs):
    if created:
        from fb_api.models import FbApiContent
        FbApiContent.objects.create(content=instance)

# In fb_api/models.py
from django.db import models
from shastra.models import Shastra

class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)


from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Shastra)
def create_fb_api_content(sender, instance, created, **kwargs):
    if created:
        FbApiContent.objects.create(content=instance)

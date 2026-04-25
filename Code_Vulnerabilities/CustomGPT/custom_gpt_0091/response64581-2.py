
from django.db.models.signals import post_save
from django.dispatch import receiver

class Shastra(models.Model):
    something = models.IntegerField()

@receiver(post_save, sender=Shastra)
def create_fb_api_content(sender, instance, created, **kwargs):
    if created:
        FbApiContent.objects.create(content=instance)

class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)

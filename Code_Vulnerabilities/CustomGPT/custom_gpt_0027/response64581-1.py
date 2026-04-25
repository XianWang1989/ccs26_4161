
from django.db import models
from django.apps import apps

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        super(Shastra, self).save(*args, **kwargs)  # Save the Shastra instance first
        self.post_content()

    def post_content(self):
        FbApiContent = apps.get_model('your_app_name', 'FbApiContent')  # Use the correct app name
        FbApiContent.objects.create(content=self)

class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra, on_delete=models.CASCADE)

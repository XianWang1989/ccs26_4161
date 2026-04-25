
# In shastra/models.py
from django.db import models
from django.apps import apps

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        self.post_content(content=self)
        super(Shastra, self).save(*args, **kwargs)

    def post_content(self, content):
        # Obtain the FbApiContent model without circular import issues
        FbApiContent = apps.get_model('fb_api', 'FbApiContent')
        FbApiContent(content=content).save()


# In fb_api/models.py
from django.db import models

class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)

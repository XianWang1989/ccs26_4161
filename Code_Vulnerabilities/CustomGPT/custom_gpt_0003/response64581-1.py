
# shastra/models.py

from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        self.post_content(content=self)
        super(Shastra, self).save(*args, **kwargs)

    def post_content(self, *args, **kwargs):  
        from fb_api.models import FbApiContent  # Local import
        FbApiContent(content=kwargs['content']).save()


# fb_api/models.py

from django.db import models

# Avoid circular import by not importing Shastra directly at the top
class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)  # Use string reference

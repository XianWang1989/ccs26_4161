
from django.db import models

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)


# Move the function definition outside of model imports to avoid circular dependencies
def post_content(*args, **kwargs):
    FbApiContent(content=kwargs['content']).save()


# Use a string reference for the ForeignKey to prevent circular imports
class FbApiContent(models.Model):
    content = models.ForeignKey('Shastra', on_delete=models.CASCADE)

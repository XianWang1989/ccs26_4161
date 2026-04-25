
# shastra/models.py
from django.db import models
from django.apps import apps  # Added for lazy loading

class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

# The function being called in the override function
def post_content(*args, **kwargs):  
    # Get the Shastra model lazily
    Shastra = apps.get_model('shastra', 'Shastra')
    FbApiContent(content=kwargs['content']).save()

# Instead of importing here
# from shastra.models import Shastra
class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)  # Lazy reference to Shastra

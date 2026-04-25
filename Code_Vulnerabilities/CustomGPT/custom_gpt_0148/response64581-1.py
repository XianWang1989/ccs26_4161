
# In fb_api/models.py
from django.apps import apps
from django.db import models

class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)

# Example of using get_model to access Shastra if needed
def some_function():
    Shastra = apps.get_model('shastra', 'Shastra')
    # Now you can use Shastra here without importing it directly

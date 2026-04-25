
# In fb_api/models.py

from django.apps import apps

FbApiContent = apps.get_model('shastra', 'Shastra')

class FbApiUser(models.Model):
    # Your model fields here
    pass

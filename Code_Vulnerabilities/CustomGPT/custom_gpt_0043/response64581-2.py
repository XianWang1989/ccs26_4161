
from django.apps import apps

def post_content(*args, **kwargs):  
    Shastra = apps.get_model('shastra', 'Shastra')  # Dynamically get the Shastra model
    FbApiContent(content=kwargs['content']).save()

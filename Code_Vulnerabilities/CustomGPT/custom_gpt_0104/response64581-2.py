
from django.apps import apps

def post_content(*args, **kwargs):
    Shastra = apps.get_model('shastra', 'Shastra')  # Dynamically get model
    FbApiContent(content=kwargs['content']).save()

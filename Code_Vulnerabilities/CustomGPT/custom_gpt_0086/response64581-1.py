
from django.apps import apps

def post_content(*args, **kwargs):
    Shastra = apps.get_model('shastra', 'Shastra')
    FbApiContent(content=kwargs['content']).save()


from django.db import models

def post_content(*args, **kwargs):
    from shastra.models import Shastra  # Deferred import here as well
    FbApiContent(content=kwargs['content']).save()

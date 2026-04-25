
# api.py in fb_api app

from .models import FbApiUser  # Import other necessary models

def post_content(*args, **kwargs):  
    from shastra.models import Shastra  # Move import here
    FbApiContent(content=kwargs['content']).save()

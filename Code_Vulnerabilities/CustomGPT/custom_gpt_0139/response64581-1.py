
# utils.py
from .models import Shastra
from fb_api.models import FbApiContent

def post_content(*args, **kwargs):  
    if 'content' in kwargs:
        FbApiContent(content=kwargs['content']).save()

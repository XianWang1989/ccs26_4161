
# utils.py
from shastra.models import Shastra
from fb_api.models import FbApiContent

def post_content(*args, **kwargs):  
    FbApiContent(content=kwargs['content']).save()

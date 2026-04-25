
# fb_api/utils.py
from shastra.models import Shastra
from .models import FbApiContent

def post_content(*args, **kwargs):
    FbApiContent(content=kwargs['content']).save()

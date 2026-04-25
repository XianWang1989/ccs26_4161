
# utils.py
from fb_api.models import FbApiContent

def post_content(content):  
    FbApiContent(content=content).save()


# fb_api/api.py
def post_content(*args, **kwargs):  
    from fb_api.models import FbApiContent  # Local import
    FbApiContent(content=kwargs['content']).save()

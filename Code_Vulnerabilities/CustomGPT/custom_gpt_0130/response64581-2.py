
# In fb_api/api.py
def post_content(*args, **kwargs):
    from shastra.models import Shastra
    FbApiContent(content=kwargs['content']).save()

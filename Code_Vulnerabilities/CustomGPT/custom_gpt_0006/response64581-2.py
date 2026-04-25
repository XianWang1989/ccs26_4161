
def post_content(*args, **kwargs):
    from fb_api.models import FbApiContent  # Lazy import
    FbApiContent(content=kwargs['content']).save()


def post_content(*args, **kwargs):
    from fb_api.models import FbApiContent  # Import here to avoid circular imports
    FbApiContent(content=kwargs['content']).save()

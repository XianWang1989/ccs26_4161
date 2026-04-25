
def post_content(*args, **kwargs):
    from shastra.models import Shastra  # Lazy import
    FbApiContent(content=kwargs['content']).save()

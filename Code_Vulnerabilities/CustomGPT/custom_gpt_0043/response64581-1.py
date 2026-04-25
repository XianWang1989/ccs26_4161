
# In your models.py or relevant file

def post_content(*args, **kwargs):
    from shastra.models import Shastra  # Moved import here to prevent circular import
    FbApiContent(content=kwargs['content']).save()

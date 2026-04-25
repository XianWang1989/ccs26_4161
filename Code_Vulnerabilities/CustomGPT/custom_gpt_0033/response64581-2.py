
from django.db import models

class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)  # Use string reference

# Optionally, define post_content here if needed
def post_content(*args, **kwargs):  
    FbApiContent(content=kwargs['content']).save()


class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)

def post_content(*args, **kwargs):  
     FbApiContent(content=kwargs['content']).save()

from shastra.models import Shastra

class FbApiContent(models.Model):
    content = models.ForeignKey(Shastra)

# The traceback you've included starts here

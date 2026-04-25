
class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(app='shastra', content=self)
        super(Shastra, self).save(*args, **kwargs)


def post_content(*args, **kwargs):
    from shastra.models import Shastra  # Moved import here
    FbApiContent(content=kwargs['content']).save()


class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)  # Keep the reference to Shastra

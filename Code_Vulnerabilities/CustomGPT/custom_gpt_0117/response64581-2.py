
class Shastra(models.Model):
    something = models.IntegerField()

    def save(self, *args, **kwargs):
        post_content(content=self)
        super().save(*args, **kwargs)

class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)

def post_content(content):  
    FbApiContent(content=content).save()

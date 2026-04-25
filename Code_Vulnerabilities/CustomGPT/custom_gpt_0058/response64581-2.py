
# In fb_api/models.py

class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)

    def some_function(self):
        from shastra.models import Shastra  # Import here to avoid circular import
        # Your function logic here

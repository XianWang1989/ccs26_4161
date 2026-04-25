
# fb_api/models.py

class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)

# Only import Shastra within the method or when needed
def some_function():
    from shastra.models import Shastra
    # Now you can use Shastra here without circular imports

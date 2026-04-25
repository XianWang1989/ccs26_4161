
class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)  # Use string reference

# Other code...

def some_function():
    from shastra.models import Shastra  # Import here
    # Use Shastra here


# Remove the import of Shastra at the top
# from shastra.models import Shastra

class FbApiContent(models.Model):
    content = models.ForeignKey('shastra.Shastra', on_delete=models.CASCADE)

# Use Shastra only when necessary within functions or methods
def some_function():
    from shastra.models import Shastra
    # Now you can use Shastra here without the circular import issue

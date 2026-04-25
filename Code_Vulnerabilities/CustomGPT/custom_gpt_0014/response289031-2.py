
class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    published = models.DateField()
    is_active = models.BooleanField(default=True)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)


class Book(models.Model):
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

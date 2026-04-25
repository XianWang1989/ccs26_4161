
class Book(models.Model):
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=255)
    published = models.DateField()

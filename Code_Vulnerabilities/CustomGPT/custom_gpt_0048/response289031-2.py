
class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    published = models.DateField()

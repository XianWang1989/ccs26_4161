
class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):  # Change `__unicode__` to `__str__`
        return self.name


class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)  # added related_name
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=255)

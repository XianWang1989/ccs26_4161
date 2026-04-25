
class Image(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)  # Specify on_delete
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=255)

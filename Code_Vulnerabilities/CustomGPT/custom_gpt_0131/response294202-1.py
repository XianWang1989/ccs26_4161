
class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)  # Set related_name
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=255)

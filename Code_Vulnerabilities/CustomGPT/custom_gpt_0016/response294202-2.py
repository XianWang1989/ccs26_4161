
class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images')  # Ensure related_name for reverse lookup
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=255)

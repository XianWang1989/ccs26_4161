
# models.py
class Gallery(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name  # Use __str__ for Python 3

class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=255)

# resources.py
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from .models import Gallery, Image

class GalleryResource(ModelResource):
    images = fields.ToManyField('your_app.resources.ImageResource', 'images', full=True)

    class Meta:
        queryset = Gallery.objects.all()
        authorization = Authorization()
        resource_name = 'gallery'

class ImageResource(ModelResource):
    gallery = fields.ForeignKey(GalleryResource, 'gallery')

    class Meta:
        queryset = Image.objects.all()
        authorization = Authorization()
        resource_name = 'images'

# Posting Example
# Use a tool like Postman or HTTPie to post JSON data:
# POST to http://127.0.0.1:8000/api/v1/images/
# {
#     "name": "My family",
#     "title": "Wassup",
#     "gallery": "/api/v1/gallery/1/"
# }

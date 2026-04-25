
from collections import defaultdict
from django.db.models import Prefetch

# Assuming your Tags model is defined like this:
class Tags(models.Model):
    name = models.CharField(max_length=100)

# Your Item model
class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tags)

# In your view
def my_view(request):
    # Prefetch items of a specific type along with associated tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a defaultdict to store the tag-item relationship
    tag_dict = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    return tag_dict

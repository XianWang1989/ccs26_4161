
from django.db.models import Prefetch
from collections import defaultdict

# Assuming you have the Item and Tags models set up
class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    tags = models.ManyToManyField('Tag')

class Tag(models.Model):
    name = models.CharField(max_length=100)

# Your view function
def my_view(request):
    # Filter items by type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Initialize a dictionary to hold tags and their corresponding items
    tag_to_items = defaultdict(list)

    # Iterate through the filtered items and build the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_to_items[tag.name].append(item)

    return tag_to_items

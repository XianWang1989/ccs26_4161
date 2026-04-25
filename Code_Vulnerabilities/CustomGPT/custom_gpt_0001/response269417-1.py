
from django.db.models import Prefetch
from collections import defaultdict

# Assuming we have the Item and Tags models
class Tags(models.Model):
    name = models.CharField(max_length=200)

class Item(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tags)

# In your view
def my_view(request):
    # Fetch items filtered by type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a dictionary to hold the result
    tag_to_items = defaultdict(list)

    # Iterate over the items and populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_to_items[tag.name].append(item)

    # Convert defaultdict back to a regular dict if needed
    tag_to_items = dict(tag_to_items)

    # Now, 'tag_to_items' contains the desired mapping
    return tag_to_items


from collections import defaultdict
from django.db.models import Prefetch

# Assuming you have a Tags model defined like this:
class Tags(models.Model):
    name = models.CharField(max_length=100)

# Your Item model
class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tags)

# Your view function
def get_items_by_tags(view_type):
    # Filter items by type and prefetch related tags
    items = Item.objects.filter(type=view_type).prefetch_related('tags')

    # Initialize a default dictionary to hold tags and their associated items
    tags_dict = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tags_dict[tag.name].append(item)

    return tags_dict

# Usage
result = get_items_by_tags('type_a')

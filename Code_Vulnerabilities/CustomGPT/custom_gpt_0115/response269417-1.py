
from django.db.models import Prefetch
from collections import defaultdict

# Assuming you have defined the Tags model properly
class Tags(models.Model):
    name = models.CharField(max_length=100)

class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tags)

def get_items_by_tags(item_type):
    # Prefetch tags for the items of a specific type
    items = Item.objects.filter(type=item_type).prefetch_related('tags')

    # Create a dictionary to hold tags and associated items
    tag_dict = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    return dict(tag_dict)

# Example usage
items_by_tags = get_items_by_tags('type_a')

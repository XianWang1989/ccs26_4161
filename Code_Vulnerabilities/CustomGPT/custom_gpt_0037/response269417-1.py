
from django.db.models import Prefetch
from collections import defaultdict

# Assuming `Tags` is your model for tags
class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    tags = models.ManyToManyField('Tags')

def get_items_by_tags(type_filter):
    # Prefetch tags related to items of the given type
    items = Item.objects.filter(type=type_filter).prefetch_related('tags')

    # Create a dictionary to hold tags as keys and items as values
    tag_to_items = defaultdict(list)

    # Iterate through items and populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_to_items[tag.name].append(item)

    return dict(tag_to_items)

# Usage
items_by_tags = get_items_by_tags('type_a')
print(items_by_tags)


from django.db.models import Prefetch
from collections import defaultdict

# Assuming the following models
class Tag(models.Model):
    name = models.CharField(max_length=255)

class Item(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)

def get_items_by_tags(type_filter):
    # Fetch items of the specified type with related tags
    items = Item.objects.filter(type=type_filter).prefetch_related('tags')

    # Create a dictionary to relate tags to items
    tag_items_map = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_items_map[tag.name].append(item)

    return dict(tag_items_map)

# Usage
items_by_tags = get_items_by_tags('type_a')
print(items_by_tags)

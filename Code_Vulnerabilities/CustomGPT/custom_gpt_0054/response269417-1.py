
from collections import defaultdict
from django.db.models import Prefetch
from .models import Item, Tags

def get_items_by_type_and_tags(type_value):
    # Prefetch related tags for each item of the specified type
    items = Item.objects.filter(type=type_value).prefetch_related('tags')

    # Create a dictionary to hold tags as keys and corresponding items as a list
    tags_dict = defaultdict(list)

    # Iterate over the items and populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tags_dict[tag.name].append(item)

    return dict(tags_dict)  # Convert defaultdict back to a regular dict

# Usage
items_by_tags = get_items_by_type_and_tags('type_a')
print(items_by_tags)

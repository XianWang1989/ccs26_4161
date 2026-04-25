
from collections import defaultdict
from django.db.models import Prefetch

# Your Item model and Tags model assumed already defined

def get_items_by_tags(type_value):
    # Prefetch tags for items of the specific type
    items = Item.objects.filter(type=type_value).prefetch_related('tags')

    # Create a dictionary to hold tag-to-item mappings
    tag_dict = defaultdict(list)

    # Iterate through each item and its tags
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    return tag_dict

# Usage
items_by_tags = get_items_by_tags('type_a')

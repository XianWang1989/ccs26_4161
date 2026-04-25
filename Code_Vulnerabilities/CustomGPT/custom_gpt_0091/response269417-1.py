
from collections import defaultdict
from django.db.models import Prefetch
from .models import Item, Tags

def get_items_by_tags():
    # Pre-fetch tags related to items of type 'type_a'
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a defaultdict to hold the tag-item relationships
    tag_item_map = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_item_map[tag.name].append(item)

    return dict(tag_item_map)

# Usage
items_by_tags = get_items_by_tags()
print(items_by_tags)

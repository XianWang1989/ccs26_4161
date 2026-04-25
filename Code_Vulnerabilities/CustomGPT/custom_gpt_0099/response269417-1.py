
from django.db.models import Prefetch
from collections import defaultdict
from .models import Item, Tags

def get_items_with_tags():
    # Prefetch related tags for items of type 'type_a'
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a dictionary to hold the tag-item mapping
    tag_item_dict = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():  # Access prefetched tags
            tag_item_dict[tag.name].append(item)

    return tag_item_dict

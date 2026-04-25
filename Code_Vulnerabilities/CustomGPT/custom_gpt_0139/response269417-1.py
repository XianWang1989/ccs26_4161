
from collections import defaultdict
from django.db.models import Prefetch
from .models import Item, Tags

def get_items_with_tags(item_type):
    # Prefetch the related Tags for Items
    items = Item.objects.filter(type=item_type).prefetch_related('tags')

    # Create a dictionary to hold the relations
    tag_to_items = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():  # Using the pre-fetched tags
            tag_to_items[tag.name].append(item)

    return dict(tag_to_items)

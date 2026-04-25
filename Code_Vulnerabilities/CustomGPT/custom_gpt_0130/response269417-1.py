
from collections import defaultdict
from django.db.models import Prefetch
from .models import Item, Tags

def get_items_by_tags(request):
    # Filter items by type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Initialize a dictionary to hold the tags and their corresponding items
    tags_to_items = defaultdict(list)

    # Iterate through items and populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tags_to_items[tag.name].append(item)

    return tags_to_items

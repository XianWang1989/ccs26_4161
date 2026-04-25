
from django.db.models import Prefetch
from .models import Item, Tags

def get_items_by_tags():
    # Fetch all items of a specific type and prefetch their tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Initialize an empty dictionary to hold tags and items
    tags_dict = {}

    # Loop through each item and organize them by their tags
    for item in items:
        for tag in item.tags.all():
            if tag.name not in tags_dict:
                tags_dict[tag.name] = []
            tags_dict[tag.name].append(item)

    return tags_dict

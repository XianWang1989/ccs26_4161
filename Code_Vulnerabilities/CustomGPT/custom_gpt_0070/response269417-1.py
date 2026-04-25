
from django.db.models import Prefetch
from .models import Item, Tags

def get_items_by_tags(type_value):
    # Use prefetch_related to fetch related tags
    items = Item.objects.filter(type=type_value).prefetch_related('tags')

    # Initialize an empty dictionary to hold tags and associated items
    tag_dict = {}

    # Iterate over the items and construct the tag dictionary
    for item in items:
        for tag in item.tags.all():
            if tag.name not in tag_dict:
                tag_dict[tag.name] = []
            tag_dict[tag.name].append(item)

    return tag_dict

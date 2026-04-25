
from django.db.models import Prefetch
from .models import Item, Tags

def get_items_by_tags():
    # Fetch items of a specific type and prefetch the related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a dictionary to hold tags and their related items
    tag_dict = {}

    for item in items:
        for tag in item.tags.all():
            if tag.name not in tag_dict:
                tag_dict[tag.name] = []
            tag_dict[tag.name].append(item)

    return tag_dict

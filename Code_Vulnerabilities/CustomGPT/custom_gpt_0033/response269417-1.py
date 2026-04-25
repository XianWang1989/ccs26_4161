
from collections import defaultdict
from django.db.models import Prefetch
from .models import Item, Tags

def get_items_by_tags():
    # Fetch items with their related tags using prefetch_related
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Initialize a defaultdict to store tags as keys and items as values
    tags_dict = defaultdict(list)

    # Iterate through the items and populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tags_dict[tag.name].append(item)

    return dict(tags_dict)


from django.db.models import Prefetch
from .models import Item, Tags

def get_items_with_tags():
    # Prefetch the related tags for items of the specified type
    items = Item.objects.filter(type='type_a').prefetch_related(Prefetch('tags'))

    # Initialize the dictionary to store tags and their corresponding items
    tags_dict = {}

    # Iterate over the items and populate the tags dictionary
    for item in items:
        for tag in item.tags.all():
            if tag.name not in tags_dict:
                tags_dict[tag.name] = []  # Create a new list for the tag
            tags_dict[tag.name].append(item)  # Append the item to the list

    return tags_dict

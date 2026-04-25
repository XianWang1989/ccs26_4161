
from django.db.models import Prefetch

def my_view(request):
    # Fetch all items of a specific type with their tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Initialize an empty dictionary to gather tags and their associated items
    tag_item_dict = {}

    # Iterate through each item and build the tag-item dictionary
    for item in items:
        for tag in item.tags.all():
            # If the tag is not already in the dictionary, initialize it
            if tag.name not in tag_item_dict:
                tag_item_dict[tag.name] = []
            # Append the item to the list of the given tag
            tag_item_dict[tag.name].append(item)

    return tag_item_dict

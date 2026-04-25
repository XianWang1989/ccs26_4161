
from django.db.models import Prefetch

# Assume you already have your items filtered by type
items = Item.objects.filter(type='type_a').prefetch_related('tags')

# Initialize a dictionary to hold tags and their corresponding items
tags_dict = {}

# Iterate through the filtered items
for item in items:
    for tag in item.tags.all():  # This fetches all tags related to the item
        if tag.name not in tags_dict:
            tags_dict[tag.name] = []  # Initialize the list if tag not in dict
        tags_dict[tag.name].append(item)  # Add the current item to the tag's list

# Now tags_dict contains the desired output

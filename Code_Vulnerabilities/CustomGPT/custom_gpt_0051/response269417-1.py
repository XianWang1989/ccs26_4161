
from django.db.models import Prefetch
from .models import Item, Tags

# Fetch the items with their related tags in one query
items = Item.objects.filter(type='type_a').prefetch_related('tags')

# Initialize the dictionary to hold tags and corresponding items
tag_to_items = {}

# Iterate through the items and populate the dictionary
for item in items:
    for tag in item.tags.all():
        if tag.name not in tag_to_items:
            tag_to_items[tag.name] = []
        tag_to_items[tag.name].append(item)

# Now tag_to_items contains the desired structure
print(tag_to_items)

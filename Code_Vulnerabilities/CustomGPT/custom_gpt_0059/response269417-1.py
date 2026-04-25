
from collections import defaultdict
from django.db.models import Prefetch

# Assume Item and Tags models are defined as in your example
# Fetch items with prefetching related tags to minimize database queries
items = Item.objects.filter(type='type_a').prefetch_related('tags')

# Create a dictionary to hold tags and their associated items
tag_to_items = defaultdict(list)

# Populate the dictionary
for item in items:
    for tag in item.tags.all():
        tag_to_items[tag.name].append(item)

# Convert defaultdict to a regular dict if desired
tag_to_items = dict(tag_to_items)

# tag_to_items now contains the mapping of tags to items
print(tag_to_items)


from collections import defaultdict
from django.db.models import Prefetch

# Assuming you already have the filtered items
items = Item.objects.filter(type='type_a').prefetch_related('tags')

# Create a defaultdict to hold tags and their corresponding items
tag_to_items = defaultdict(list)

# Iterate through the items and build the dictionary
for item in items:
    for tag in item.tags.all():
        tag_to_items[tag.name].append(item)

# Converting defaultdict to a regular dict (optional)
tag_to_items = dict(tag_to_items)

# Now tag_to_items contains the desired mapping

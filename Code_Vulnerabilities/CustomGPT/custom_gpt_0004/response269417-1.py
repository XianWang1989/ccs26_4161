
from collections import defaultdict
from django.db.models import Prefetch

# Fetch items with prefetch for related tags
items = Item.objects.filter(type='type_a').prefetch_related('tags')

# Initialize a dictionary to hold the tags and their associated items
tag_to_items = defaultdict(list)

# Iterate through the items and populate the dictionary
for item in items:
    for tag in item.tags.all():
        tag_to_items[tag.name].append(item)

# Example output structure
print(dict(tag_to_items))

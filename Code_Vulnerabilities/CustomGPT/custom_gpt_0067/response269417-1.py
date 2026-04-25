
from collections import defaultdict
from django.db.models import Prefetch

# Retrieve items of a specific type with their related tags
items = Item.objects.filter(type='type_a').prefetch_related('tags')

# Initialize a defaultdict to hold tags and corresponding items
tag_dict = defaultdict(list)

# Populate the dictionary
for item in items:
    for tag in item.tags.all():
        tag_dict[tag.name].append(item)

# Convert defaultdict to a regular dictionary if needed
tag_dict = dict(tag_dict)

# Example output
print(tag_dict)

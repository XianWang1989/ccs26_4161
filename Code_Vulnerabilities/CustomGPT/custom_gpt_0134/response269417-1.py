
from collections import defaultdict
from django.db.models import Prefetch

# Fetch all items of a specific type with their related tags
items = Item.objects.filter(type='type_a').prefetch_related('tags')

# Initialize a defaultdict to store tags and associated items
tag_to_items = defaultdict(list)

# Populate the dictionary
for item in items:
    for tag in item.tags.all():
        tag_to_items[tag.name].append(item)

# Convert defaultdict to a regular dict (optional)
tag_to_items = dict(tag_to_items)

# Now `tag_to_items` contains the desired mapping
print(tag_to_items)


from django.db.models import Prefetch
from collections import defaultdict
from .models import Item, Tags

# Fetch items with prefetching tags
items = Item.objects.filter(type='type_a').prefetch_related('tags')

# Create a dictionary to hold tags and their corresponding items
tag_dict = defaultdict(list)

# Populate the dictionary
for item in items:
    for tag in item.tags.all():
        tag_dict[tag.name].append(item)

# Convert defaultdict to regular dict if needed
tag_dict = dict(tag_dict)

# Output example
print(tag_dict)


from collections import defaultdict
from django.db.models import Prefetch

# Assuming 'type_a' is the type you want to filter
items = Item.objects.filter(type='type_a').prefetch_related('tags')

# Create a default dictionary to hold tags and their associated items
tagged_items = defaultdict(list)

# Populate the dictionary
for item in items:
    for tag in item.tags.all():
        tagged_items[tag.name].append(item)

# Convert defaultdict to a regular dict if needed
tagged_items = dict(tagged_items)

# Example output
print(tagged_items)

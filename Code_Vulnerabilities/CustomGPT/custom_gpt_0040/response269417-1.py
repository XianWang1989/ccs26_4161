
from django.db.models import Prefetch
from collections import defaultdict

# Assuming you have already filtered items
items_query = Item.objects.filter(type='type_a').prefetch_related('tags')

# Initialize a dictionary to hold the results
tags_to_items = defaultdict(list)

# Populate the dictionary
for item in items_query:
    for tag in item.tags.all():
        tags_to_items[tag.name].append(item)

# Convert defaultdict to a regular dict if needed
tags_to_items = dict(tags_to_items)

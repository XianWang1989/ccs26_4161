
from collections import defaultdict
from django.db.models import Prefetch

# Assuming you want to filter for 'type_a'
items = Item.objects.prefetch_related('tags').filter(type='type_a')

# Create a defaultdict to hold tags as keys and lists of items as values
tags_to_items = defaultdict(list)

# Populate the dictionary
for item in items:
    for tag in item.tags.all():
        tags_to_items[tag.name].append(item)

# Convert defaultdict to a regular dict if needed
tags_to_items = dict(tags_to_items)

# Now tags_to_items is structured like:
# {
#     'tag1': [item1, item2, item5],
#     'tag2': [item1, item4],
#     'tag3': [item3, item5]
# }

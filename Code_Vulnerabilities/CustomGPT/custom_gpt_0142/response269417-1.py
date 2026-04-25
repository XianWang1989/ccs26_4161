
from collections import defaultdict
from django.db.models import Prefetch

# Step 1: Filter items by type and prefetch related tags
items = Item.objects.filter(type='type_a').prefetch_related('tags')

# Step 2: Create a dictionary to hold tags and their corresponding items
tagged_items = defaultdict(list)

# Step 3: Populate the dictionary
for item in items:
    for tag in item.tags.all():
        tagged_items[tag.name].append(item)

# tagged_items now contains the desired output
# Example structure:
# {
#     'tag1': [item1, item2, item5],
#     'tag2': [item1, item4],
#     'tag3': [item3, item5]
# }

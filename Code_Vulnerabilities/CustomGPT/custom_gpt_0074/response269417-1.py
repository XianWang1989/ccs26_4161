
from collections import defaultdict
from django.db.models import Prefetch

# Assuming you have the 'type_a' filter set as in your question:
items = Item.objects.filter(type='type_a').prefetch_related('tags')

# Create a default dictionary to hold tags and their related items
tag_to_items = defaultdict(list)

# Loop through each item and append it to the corresponding tags
for item in items:
    for tag in item.tags.all():  # Access the related tags
        tag_to_items[tag.name].append(item)

# Convert defaultdict back to a regular dict, if needed
tag_to_items = dict(tag_to_items)

print(tag_to_items)

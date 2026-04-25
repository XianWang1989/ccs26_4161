
from collections import defaultdict
from django.db.models import Prefetch

# Assuming you have already defined your Item and Tag models
# First, fetch the items with the specified type and prefetch the related tags
items = Item.objects.filter(type='type_a').prefetch_related('tags')

# Create a defaultdict to store tags and their associated items
tag_item_dict = defaultdict(list)

# Iterate through the items and populate the dictionary
for item in items:
    for tag in item.tags.all():
        tag_item_dict[tag.name].append(item)

# Convert defaultdict to a regular dict if needed
tag_item_dict = dict(tag_item_dict)

# Now tag_item_dict contains the desired output
print(tag_item_dict)

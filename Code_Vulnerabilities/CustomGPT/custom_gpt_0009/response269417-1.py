
from django.db.models import Prefetch

# First, filter the items by type and use prefetch_related to get the tags
items = Item.objects.filter(type='type_a').prefetch_related('tags')

# Initialize the dictionary
tag_to_items = {}

# Iterate through the items and populate the dictionary
for item in items:
    for tag in item.tags.all():  # This will not hit the database again because of prefetch_related
        if tag.name not in tag_to_items:
            tag_to_items[tag.name] = []
        tag_to_items[tag.name].append(item)

# Now tag_to_items contains the relationship you're looking for!

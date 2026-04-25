from collections import defaultdict
from django.db.models import Prefetch

# Prefetch tags efficiently
items = Item.objects.filter(type='type_a').prefetch_related('tags')

# Create the tag to items dictionary
tag_to_items = defaultdict(list)

for item in items:
    for tag in item.tags.all():
        tag_to_items[tag.name].append(item)

# Now tag_to_items will be in the desired format
print(dict(tag_to_items))

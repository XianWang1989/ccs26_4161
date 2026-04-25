
from collections import defaultdict
from django.db.models import Prefetch

# Fetch items of a specific type while prefetching their related tags
items = Item.objects.filter(type='type_a').prefetch_related('tags')

# Initialize a dictionary to relate tags to items
tag_to_items = defaultdict(list)

# Iterate over the items and populate the dictionary
for item in items:
    for tag in item.tags.all():
        tag_to_items[tag.name].append(item)

# The resulting dictionary: tag_to_items

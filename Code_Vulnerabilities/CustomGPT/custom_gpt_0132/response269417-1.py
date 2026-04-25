
from collections import defaultdict
from django.db.models import Prefetch
from .models import Item, Tags

# Step 1: Filter and prefetched related tags
items = Item.objects.filter(type='type_a').prefetch_related('tags')

# Step 2: Create a defaultdict to store tags and corresponding items
tag_to_items = defaultdict(list)

# Step 3: Populate the dictionary
for item in items:
    for tag in item.tags.all():  # Accessing prefetched tags
        tag_to_items[tag.name].append(item)

# Now tag_to_items contains the required dictionary

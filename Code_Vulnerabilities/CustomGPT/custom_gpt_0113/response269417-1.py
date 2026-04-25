
from collections import defaultdict
from django.db.models import Prefetch

# Fetch items of a specific type with their related tags
items = Item.objects.filter(type='type_a').prefetch_related('tags')

# Create a dictionary to relate tags to items
tag_dict = defaultdict(list)

# Populate the dictionary
for item in items:
    for tag in item.tags.all():
        tag_dict[tag.name].append(item)

# Now `tag_dict` contains the desired structure

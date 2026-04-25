
from collections import defaultdict
from django.db.models import Prefetch

# Fetch items of a specific type and prefetch their related tags
items = Item.objects.filter(type='type_a').prefetch_related('tags')

# Initialize a defaultdict to hold the tags and their corresponding items
tag_dict = defaultdict(list)

# Populate the dictionary
for item in items:
    for tag in item.tags.all():
        tag_dict[tag.name].append(item)

# Now tag_dict will contain the desired output
# Example output:
# {
#     'tag1': [item1, item2, item5],
#     'tag2': [item1, item4],
#     'tag3': [item3, item5]
# }

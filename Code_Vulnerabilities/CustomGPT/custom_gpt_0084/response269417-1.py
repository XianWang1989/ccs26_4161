
from collections import defaultdict
from django.db.models import Prefetch

# Assuming you have a model `Tags`
# Fetch items and prefetch their tags
items = Item.objects.filter(type='type_a').prefetch_related('tags')

# Initialize a defaultdict for storing tags related to items
tag_dict = defaultdict(list)

# Iterate through items and populate the dictionary
for item in items:
    for tag in item.tags.all():
        tag_dict[tag.name].append(item)

# Now, tag_dict contains the desired output
print(dict(tag_dict))  # Convert defaultdict to dict for a nicer output

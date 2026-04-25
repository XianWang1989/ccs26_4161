
from django.db.models import Prefetch

# Fetch items with their related tags using prefetch_related
items = Item.objects.filter(type='type_a').prefetch_related('tags')

# Initialize an empty dictionary to store tags and their related items
tag_dict = {}

# Populate the dictionary
for item in items:
    for tag in item.tags.all():
        if tag.name not in tag_dict:
            tag_dict[tag.name] = []
        tag_dict[tag.name].append(item)

# Output: Dictionary relating tags to items
print(tag_dict)

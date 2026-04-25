
from django.db.models import Prefetch
from collections import defaultdict

# Assuming you have imported the necessary models
def get_items_by_tags(type_name):
    # Use prefetch_related to retrieve tags for each item efficiently
    items = Item.objects.filter(type=type_name).prefetch_related('tags')

    tag_dict = defaultdict(list)

    # Populate the dictionary with tags as keys and items as values
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    return dict(tag_dict)  # Convert defaultdict to a regular dict

# Usage example
items_by_tags = get_items_by_tags('type_a')
print(items_by_tags)

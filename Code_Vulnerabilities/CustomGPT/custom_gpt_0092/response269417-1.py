
from collections import defaultdict
from django.db.models import Prefetch

# Assuming Tags is your model for tags
from .models import Item, Tags

def get_items_by_tags(request):
    # Filter the Items by type and prefetch related Tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a dictionary to hold the relationship
    tags_to_items = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tags_to_items[tag.name].append(item)

    return tags_to_items


from django.db.models import Prefetch
from collections import defaultdict

def your_view(request):
    # Fetch the items and prefetch their tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a dictionary to hold tags and corresponding items
    tags_dict = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tags_dict[tag.name].append(item)

    return tags_dict

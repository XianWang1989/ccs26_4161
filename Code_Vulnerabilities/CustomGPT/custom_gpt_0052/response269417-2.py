
from django.db.models import Prefetch
from collections import defaultdict

def get_items_by_tags(request):
    # Filter items by type
    filtered_items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a dictionary to relate tags to items
    tag_dict = defaultdict(list)

    for item in filtered_items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    return tag_dict

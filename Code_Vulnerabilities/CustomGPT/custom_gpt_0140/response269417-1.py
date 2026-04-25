
from django.db.models import Prefetch
from .models import Item, Tags

def get_items_with_tags():
    # Prefetch tags related to items of type 'type_a'
    items = Item.objects.filter(type='type_a').prefetch_related(
        Prefetch('tags')
    )

    # Create a dictionary to map tags to items
    tag_to_items = {}

    for item in items:
        for tag in item.tags.all():
            if tag.name not in tag_to_items:
                tag_to_items[tag.name] = []
            tag_to_items[tag.name].append(item)

    return tag_to_items


from django.db.models import Prefetch
from .models import Item, Tag

def get_items_with_tags(request):
    # Filter items by type
    items = Item.objects.filter(type='type_a').prefetch_related(
        Prefetch('tags')
    )

    # Build the dictionary of tags to items
    tag_to_items = {}
    for item in items:
        for tag in item.tags.all():
            if tag.name not in tag_to_items:
                tag_to_items[tag.name] = []
            tag_to_items[tag.name].append(item)

    return tag_to_items

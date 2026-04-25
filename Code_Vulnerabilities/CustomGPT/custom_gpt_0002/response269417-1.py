
from collections import defaultdict
from .models import Item

def get_items_by_tags():
    items = Item.objects.filter(type='type_a').prefetch_related('tags')
    tag_dict = defaultdict(list)

    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    return dict(tag_dict)

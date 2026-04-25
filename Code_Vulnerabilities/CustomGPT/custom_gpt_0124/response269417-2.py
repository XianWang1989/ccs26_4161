
from django.db.models import Prefetch
from collections import defaultdict

def your_view(request):
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    tag_to_items = defaultdict(list)

    for item in items:
        for tag in item.tags.all():
            tag_to_items[tag.name].append(item)

    return tag_to_items

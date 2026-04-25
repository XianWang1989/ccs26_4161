
from django.db.models import Prefetch

def get_items_by_tags(type_filter):
    items = Item.objects.filter(type=type_filter).prefetch_related('tags')
    tag_dict = {}

    for item in items:
        for tag in item.tags.all():
            if tag.name not in tag_dict:
                tag_dict[tag.name] = []
            tag_dict[tag.name].append(item)

    return tag_dict

# Usage
result = get_items_by_tags('type_a')
print(result)

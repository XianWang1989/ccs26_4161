
from collections import defaultdict
from django.db.models import Prefetch

# View function
def get_items_by_tags(request):
    # Fetch items of type 'type_a' and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    tag_dict = defaultdict(list)  # Create a default dictionary to hold tags and items

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    return tag_dict


from collections import defaultdict
from django.shortcuts import render
from .models import Item

def my_view(request):
    # Filter items based on type
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a defaultdict to store tags and corresponding items
    tag_to_items = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_to_items[tag.name].append(item)

    # Now `tag_to_items` contains the desired mapping
    context = {
        'tag_item_map': dict(tag_to_items)
    }

    return render(request, 'my_template.html', context)

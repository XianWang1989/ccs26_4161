
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def items_view(request):
    # Step 1: Filter items by type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Step 2: Initialize a dictionary to store tags and corresponding items
    tag_to_items = defaultdict(list)

    # Step 3: Populate the dictionary
    for item in items:
        for tag in item.tags.all():  # Here .all() does not hit the database again due to prefetch_related
            tag_to_items[tag.name].append(item)

    # Now `tag_to_items` contains the desired structure
    context = {
        'tag_to_items': dict(tag_to_items)  # If you want a regular dict instead of defaultdict
    }

    return render(request, 'your_template.html', context)

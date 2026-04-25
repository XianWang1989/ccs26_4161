
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def item_view(request):
    # Filter items by type
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a dictionary to hold tags and their related items
    tag_to_items = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_to_items[tag.name].append(item)

    context = {
        'tag_to_items': dict(tag_to_items)  # Convert defaultdict to a regular dict for rendering
    }

    return render(request, 'your_template.html', context)

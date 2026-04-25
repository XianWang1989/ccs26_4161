
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def your_view(request):
    # Filter items based on type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Initialize a defaultdict to store tags and their corresponding items
    tag_to_items = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_to_items[tag.name].append(item)

    # Convert defaultdict back to a regular dict if needed
    tag_to_items = dict(tag_to_items)

    context = {
        'tag_to_items': tag_to_items,
    }
    return render(request, 'your_template.html', context)

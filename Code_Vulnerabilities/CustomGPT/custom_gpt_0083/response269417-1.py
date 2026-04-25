
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def your_view(request):
    # Filter items by type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Initialize a defaultdict to hold the tags
    tag_to_items = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_to_items[tag.name].append(item)

    # Convert defaultdict to a regular dict (optional)
    tag_to_items = dict(tag_to_items)

    # Render your template with the context
    return render(request, 'your_template.html', {'tag_to_items': tag_to_items})

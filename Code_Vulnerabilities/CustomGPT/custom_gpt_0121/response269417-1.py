
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def item_view(request):
    # Filter items by type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Initialize a defaultdict to store tags and their associated items
    tag_dict = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    # Convert defaultdict to a regular dict for the final output (if needed)
    tag_dict = dict(tag_dict)

    return render(request, 'template.html', {'tag_dict': tag_dict})

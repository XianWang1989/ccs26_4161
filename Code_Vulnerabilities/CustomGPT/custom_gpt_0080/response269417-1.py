
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def items_with_tags_view(request):
    # Filter items by type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a dictionary to hold tags and their associated items
    tag_dict = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    # Optionally convert defaultdict to a standard dict
    tag_dict = dict(tag_dict)

    return render(request, 'your_template.html', {'tag_dict': tag_dict})

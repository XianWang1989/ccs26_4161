
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def your_view(request):
    # Filter items by type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Initialize a defaultdict to hold the output
    tags_dict = defaultdict(list)

    # Iterate through items and populate the tags_dict
    for item in items:
        for tag in item.tags.all():
            tags_dict[tag.name].append(item)

    # Convert defaultdict to a regular dict for final output
    result = dict(tags_dict)

    return render(request, 'your_template.html', {'tags_dict': result})

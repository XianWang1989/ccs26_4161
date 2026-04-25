
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def items_by_tag_view(request):
    # Fetch the items of a specific type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Initialize a defaultdict to hold the tags and their corresponding items
    tag_dict = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    # Convert defaultdict back to a regular dict (if needed)
    tag_dict = dict(tag_dict)

    return render(request, 'your_template.html', {'tag_dict': tag_dict})

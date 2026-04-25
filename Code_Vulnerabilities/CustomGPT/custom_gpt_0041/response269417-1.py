
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def my_view(request):
    # Filter items by type
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a dictionary to hold tags and their related items
    tag_dict = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    # Convert defaultdict to a regular dictionary if needed
    tag_dict = dict(tag_dict)

    return render(request, 'my_template.html', {'tag_dict': tag_dict})

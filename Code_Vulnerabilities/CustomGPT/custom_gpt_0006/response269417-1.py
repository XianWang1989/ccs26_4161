
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def my_view(request):
    # Filter items by type
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a dictionary to hold tags and corresponding items
    tags_dict = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tags_dict[tag.name].append(item)

    # Optionally, convert defaultdict to a normal dict
    tags_dict = dict(tags_dict)

    # Now you can render your context with `tags_dict`
    return render(request, 'my_template.html', {'tags_dict': tags_dict})

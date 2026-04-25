
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def item_view(request):
    # Filter items by type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Initialize a defaultdict to group items by their tags
    tag_to_items = defaultdict(list)

    # Iterate over the filtered items and populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_to_items[tag.name].append(item)

    # Now `tag_to_items` contains the desired output
    return render(request, 'template.html', {'tag_to_items': tag_to_items})

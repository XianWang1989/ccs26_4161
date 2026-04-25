
from collections import defaultdict
from django.shortcuts import render

def my_view(request):
    # Filter items by type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Initialize a dictionary to hold tags and corresponding items
    tag_to_items = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_to_items[tag.name].append(item)

    # Return or render the context
    return render(request, 'my_template.html', {'tag_to_items': tag_to_items})

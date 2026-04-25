
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def item_list_view(request):
    # Filter items by type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a default dictionary to hold tags and their corresponding items
    tag_dict = defaultdict(list)

    # Iterate through the filtered items and their tags
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    # Convert defaultdict to a regular dictionary if needed
    tag_dict = dict(tag_dict)

    # Assuming you want to render this in a template
    return render(request, 'your_template.html', {'tag_dict': tag_dict})

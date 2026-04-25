
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def item_tags_view(request):
    # Filter items by type
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a dictionary to hold tags and their related items
    tag_dict = defaultdict(list)

    # Loop through the items and associate tags with their items
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    # Convert defaultdict back to a regular dict if needed
    tag_dict = dict(tag_dict)

    # Pass tag_dict to the template or process it as needed
    return render(request, 'your_template.html', {'tag_dict': tag_dict})

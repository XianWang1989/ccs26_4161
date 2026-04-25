
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def item_view(request):
    # Filter items by type
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a dictionary to hold tags and their corresponding items
    tag_dict = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    # Convert defaultdict to a regular dict if needed
    tag_dict = dict(tag_dict)

    # Render your template with the tag_dict
    return render(request, 'your_template.html', {'tag_dict': tag_dict})

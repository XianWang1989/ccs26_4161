
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def items_by_tags_view(request):
    # Fetch items of type 'type_a' and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a defaultdict to hold tags as keys and related items as values
    tags_dict = defaultdict(list)

    # Loop through the items and populate the tags_dict
    for item in items:
        for tag in item.tags.all():
            tags_dict[tag.name].append(item)

    # Convert defaultdict to a regular dict if needed
    tags_dict = dict(tags_dict)

    # Render your view with the tags_dict
    return render(request, 'your_template.html', {'tags_dict': tags_dict})

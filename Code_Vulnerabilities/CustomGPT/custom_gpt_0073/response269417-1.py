
from collections import defaultdict
from django.shortcuts import render
from .models import Item, Tags

def items_by_tag_view(request):
    # Filter items by type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a dictionary to hold tags and their corresponding items
    tag_dict = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    # Render your response or return the dictionary
    return render(request, 'template.html', {'tag_dict': dict(tag_dict)})

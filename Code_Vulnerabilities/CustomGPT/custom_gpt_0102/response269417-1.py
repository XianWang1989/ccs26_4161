
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def items_by_tag_view(request):
    # Filter items by type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Initialize a defaultdict to store tags and their corresponding items
    tags_dict = defaultdict(list)

    # Iterate through the items and build the dictionary
    for item in items:
        for tag in item.tags.all():
            tags_dict[tag.name].append(item)

    return render(request, 'your_template.html', {'tags_dict': tags_dict})

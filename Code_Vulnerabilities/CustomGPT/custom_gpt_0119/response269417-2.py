
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def items_by_tags_view(request):
    # Filter items by type
    items = Item.objects.filter(item_type='type_a').prefetch_related('tags')

    # Initialize a defaultdict to construct the desired output
    tags_dict = defaultdict(list)

    # Loop through items and categorize them by tags
    for item in items:
        for tag in item.tags.all():
            tags_dict[tag.name].append(item)

    return render(request, 'template_name.html', {'tags_dict': tags_dict})

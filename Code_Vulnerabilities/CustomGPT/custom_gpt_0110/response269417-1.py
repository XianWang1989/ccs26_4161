
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def get_items_by_tags(request):
    # Filter items by type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Initialize a defaultdict to hold tags and their corresponding items
    tag_dict = defaultdict(list)

    # Iterate through items and populate the dictionary
    for item in items:
        for tag in item.tags.all():  # Access tags efficiently using prefetch_related
            tag_dict[tag.name].append(item)

    # Convert defaultdict to a regular dict if necessary
    tag_dict = dict(tag_dict)

    context = {
        'items_by_tags': tag_dict,
    }

    return render(request, 'your_template.html', context)

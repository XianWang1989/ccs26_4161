
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def items_by_tag_view(request):
    # Step 1: Filter items by type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Step 2: Create a defaultdict to hold the tags and associated items
    tag_dict = defaultdict(list)

    # Step 3: Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    # Step 4: The result is a dict where each tag maps to a list of items
    return render(request, 'your_template.html', {'tagged_items': tag_dict})

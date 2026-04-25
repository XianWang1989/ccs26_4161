
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def item_view(request):
    # Step 1: Fetch the items with the specified type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Step 2: Create a defaultdict to hold the tags and their corresponding items
    tag_to_items = defaultdict(list)

    # Step 3: Iterate through the items and populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_to_items[tag.name].append(item)

    # Now 'tag_to_items' will contain the desired output
    context = {'tag_to_items': dict(tag_to_items)}  # Convert to regular dict if needed
    return render(request, 'your_template.html', context)

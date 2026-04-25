
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def my_view(request):
    # Step 1: Fetch all items of a specific type, prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Step 2: Create a default dictionary to store tags and associated items
    tag_to_items = defaultdict(list)

    # Step 3: Iterate through the items and their tags to fill the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_to_items[tag.name].append(item)

    # Step 4: Return the dictionary as part of your response or context
    context = {
        'tag_to_items': tag_to_items,
    }
    return render(request, 'my_template.html', context)


from collections import defaultdict
from django.shortcuts import render
from .models import Item

def your_view(request):
    # Fetch items of a specific type and prefetch their related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a dictionary to relate tags to items
    tag_to_items = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_to_items[tag.name].append(item)

    # Pass the dictionary to your context
    context = {
        'tag_to_items': tag_to_items
    }
    return render(request, 'your_template.html', context)

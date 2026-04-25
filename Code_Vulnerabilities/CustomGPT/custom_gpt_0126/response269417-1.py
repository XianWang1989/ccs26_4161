
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def your_view(request):
    # Fetch items based on type with related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a dictionary to map tags to items
    tag_to_items = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_to_items[tag.name].append(item)

    # Now you can pass tag_to_items to your template or use it as needed
    return render(request, 'your_template.html', {'tag_to_items': tag_to_items})

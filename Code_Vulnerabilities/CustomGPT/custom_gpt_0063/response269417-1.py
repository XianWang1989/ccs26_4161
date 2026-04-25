
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def your_view(request):
    # Filter the items by type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a dictionary to relate Tags to Items
    tag_to_items = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_to_items[tag.name].append(item)

    # You can now use tag_to_items in your template context
    context = {
        'tag_to_items': tag_to_items,
    }

    return render(request, 'your_template.html', context)

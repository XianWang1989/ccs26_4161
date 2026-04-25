
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def your_view(request):
    # Assuming 'type_a' is the type you want to filter by
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a dictionary to hold tags related to items
    tags_to_items = defaultdict(list)

    # Loop through the items and populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tags_to_items[tag.name].append(item)

    # Render your response, passing the dictionary to the template
    return render(request, 'your_template.html', {'tags_to_items': tags_to_items})

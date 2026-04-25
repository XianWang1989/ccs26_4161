
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def my_view(request):
    # Filter items by type
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a dictionary to store tags related to items
    tag_dict = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    context = {
        'tag_dict': dict(tag_dict),  # Convert defaultdict to a regular dict
    }

    return render(request, 'my_template.html', context)

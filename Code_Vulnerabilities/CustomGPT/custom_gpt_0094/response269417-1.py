
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def my_view(request):
    # Step 1: Fetch items of a specific type with related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Step 2: Create a dictionary to hold tags and their related items
    tag_dict = defaultdict(list)

    # Step 3: Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    # Now tag_dict holds the desired structure
    return render(request, 'my_template.html', {'tag_dict': tag_dict})

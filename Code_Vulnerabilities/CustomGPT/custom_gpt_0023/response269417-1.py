
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def items_by_tag_view(request):
    # Fetch items of a specific type with related tags, optimizing queries
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Initialize a default dictionary to hold the tags and their corresponding items
    tag_dict = defaultdict(list)

    # Iterate through the items and populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    # Now `tag_dict` contains the desired mapping of tags to items
    return render(request, 'your_template.html', {'tag_dict': tag_dict})

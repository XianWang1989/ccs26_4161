
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def items_by_tags_view(request):
    # Fetch items filtered by type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a defaultdict to hold the tags and associated items
    tags_dict = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tags_dict[tag.name].append(item)

    # Convert defaultdict to regular dict for the output
    tags_dict = dict(tags_dict)

    return render(request, 'your_template.html', {'tags_dict': tags_dict})

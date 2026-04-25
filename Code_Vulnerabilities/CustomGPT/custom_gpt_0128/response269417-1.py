
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def item_list_view(request):
    # Fetch items of type 'type_a' and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Initialize a defaultdict to create the desired structure
    tags_dict = defaultdict(list)

    # Iterate over items and populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tags_dict[tag.name].append(item)

    # Convert defaultdict to a regular dict if needed
    tags_dict = dict(tags_dict)

    # Pass the dictionary to your template or handle as needed
    return render(request, 'your_template.html', {'tags_dict': tags_dict})

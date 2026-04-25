
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def my_view(request):
    # Fetch items of type 'type_a' and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a dictionary to hold tags and associated items
    tag_dict = defaultdict(list)

    # Iterate over items and populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    # Optionally render the dictionary in your template
    return render(request, 'my_template.html', {'tag_dict': tag_dict})

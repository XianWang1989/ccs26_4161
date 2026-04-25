
from django.shortcuts import render
from .models import Item

def my_view(request):
    # Filter items by type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Initialize the dictionary to hold tags and associated items
    tag_dict = {}

    # Loop through the items and populate the dictionary
    for item in items:
        for tag in item.tags.all():
            if tag.name not in tag_dict:
                tag_dict[tag.name] = []
            tag_dict[tag.name].append(item)

    return render(request, 'my_template.html', {'tag_dict': tag_dict})

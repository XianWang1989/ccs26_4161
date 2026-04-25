
from django.shortcuts import render
from .models import Item

def your_view(request):
    # Fetch items of a specific type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Initialize a dictionary to hold tags as keys and their associated items as values
    tags_dict = {}

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            if tag.name not in tags_dict:
                tags_dict[tag.name] = []
            tags_dict[tag.name].append(item)

    return render(request, 'your_template.html', {'tags_dict': tags_dict})

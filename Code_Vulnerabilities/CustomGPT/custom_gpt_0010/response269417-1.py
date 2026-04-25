
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def get_items_by_tags(request):
    # Filter items by type
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a defaultdict to collect items under their tags
    tag_dict = defaultdict(list)

    # Iterate over the filtered items
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    # Convert defaultdict to a regular dict if needed
    tag_dict = dict(tag_dict)

    # Render the context to your template
    return render(request, 'your_template.html', {'tag_dict': tag_dict})

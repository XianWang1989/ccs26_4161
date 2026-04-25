
from collections import defaultdict
from django.shortcuts import render
from .models import Item, Tags

def your_view(request):
    # Fetch items of type 'type_a' along with their tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Initialize a default dictionary to hold tags and their corresponding items
    tag_to_items = defaultdict(list)

    # Iterate over each item and their associated tags to build the desired dictionary
    for item in items:
        for tag in item.tags.all():
            tag_to_items[tag.name].append(item)

    # Convert defaultdict to a regular dict if needed
    tag_to_items = dict(tag_to_items)

    # Now you can pass `tag_to_items` to your template/context
    return render(request, 'your_template.html', {'tag_to_items': tag_to_items})

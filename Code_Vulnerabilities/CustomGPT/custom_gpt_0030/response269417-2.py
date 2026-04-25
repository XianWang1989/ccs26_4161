
from django.shortcuts import render
from collections import defaultdict

def item_view(request):
    # Retrieve all items of a specific type, prefetching related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a dictionary to relate tags to items
    tag_item_dict = defaultdict(list)

    # Build the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_item_dict[tag.name].append(item)

    # Convert defaultdict to a regular dict if needed
    tag_item_dict = dict(tag_item_dict)

    # Your response can include tag_item_dict to render in the template
    return render(request, 'your_template.html', {'tag_item_dict': tag_item_dict})

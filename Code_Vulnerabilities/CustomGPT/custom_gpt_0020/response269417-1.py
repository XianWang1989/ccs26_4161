
from collections import defaultdict
from django.shortcuts import render
from .models import Item

def my_view(request):
    # Fetch all items of type 'type_a' and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a default dictionary to hold tags and their corresponding items
    tag_dict = defaultdict(list)

    # Iterate over the items to populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    # Convert to a normal dictionary if needed
    result = dict(tag_dict)

    # Pass the result to the template or render the response as needed
    return render(request, 'my_template.html', {'tag_items': result})

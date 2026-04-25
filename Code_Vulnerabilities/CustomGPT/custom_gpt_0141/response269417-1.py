
from django.db.models import Prefetch
from collections import defaultdict

# Example view function
def my_view(request):
    # Step 1: Filter items by type and prefetch their related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Step 2: Initialize a defaultdict to hold the dictionary of tags to items
    tags_to_items = defaultdict(list)

    # Step 3: Iterate through the items and their tags
    for item in items:
        for tag in item.tags.all():
            tags_to_items[tag.name].append(item)

    # Convert defaultdict to regular dict, if needed
    tags_to_items = dict(tags_to_items)

    # Now `tags_to_items` contains the desired output
    # You can return this in your context or render accordingly
    return render(request, 'my_template.html', {'tags_to_items': tags_to_items})

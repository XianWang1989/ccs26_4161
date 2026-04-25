
from django.db.models import Prefetch

# In your view function
def get_items_with_tags(request):
    # Fetch items of a specific type with their related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Initialize a dictionary to relate tags to items
    tag_dict = {}

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            if tag.name not in tag_dict:
                tag_dict[tag.name] = []
            tag_dict[tag.name].append(item)

    return tag_dict

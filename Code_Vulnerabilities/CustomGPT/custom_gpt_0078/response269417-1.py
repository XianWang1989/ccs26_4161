
from collections import defaultdict
from django.db.models import Prefetch

# Assuming you have a Tag model defined as follows
class Tag(models.Model):
    name = models.CharField(max_length=100)

# Your view
def my_view(request):
    # Fetch items of a specific type with related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a dictionary to hold tags and corresponding items
    tag_dict = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    return tag_dict

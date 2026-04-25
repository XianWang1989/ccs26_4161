
from collections import defaultdict
from django.db.models import Prefetch

# Assuming you have a Tags model defined similarly
class Tags(models.Model):
    name = models.CharField(max_length=100)

# Your view function
def get_items_with_tags():
    # Fetch items of type 'type_a' along with their tags in a single query
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a dictionary to hold tags and their associated items
    tags_dict = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tags_dict[tag.name].append(item)

    return tags_dict


from collections import defaultdict
from django.db.models import Prefetch

# Assuming you have the following models defined
class Item(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    tags = models.ManyToManyField('Tags')

class Tags(models.Model):
    name = models.CharField(max_length=100)

# Your view function
def get_items_with_tags(view_type):
    # Fetch items of a specific type and prefetch related tags
    items = Item.objects.filter(type=view_type).prefetch_related('tags')

    # Dictionary to hold tags and corresponding items
    tags_dict = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tags_dict[tag.name].append(item)

    return dict(tags_dict)

# Usage
result = get_items_with_tags('type_a')


from collections import defaultdict
from django.db.models import Prefetch

# Assume you have the following models
class Tags(models.Model):
    name = models.CharField(max_length=100)

class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tags)

def get_items_by_type_and_tags(item_type):
    # Prefetch related tags to minimize database queries
    items = Item.objects.filter(type=item_type).prefetch_related('tags')

    # Create a defaultdict to store tags and their related items
    tag_item_dict = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_item_dict[tag.name].append(item)

    return dict(tag_item_dict)

# Example usage
items_by_tags = get_items_by_type_and_tags('type_a')
print(items_by_tags)

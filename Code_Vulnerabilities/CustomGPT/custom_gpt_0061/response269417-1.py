
from collections import defaultdict
from django.db.models import Prefetch

# Assuming your models are defined as follows
class Item(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    tags = models.ManyToManyField('Tags')

class Tags(models.Model):
    name = models.CharField(max_length=255)

def get_items_by_tag(item_type):
    # Prefetch tags to avoid extra queries for each item
    items = Item.objects.filter(type=item_type).prefetch_related('tags')

    # Create a dictionary to hold tags and their corresponding items
    tag_dict = defaultdict(list)

    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    return dict(tag_dict)

# Example usage
items_by_tag = get_items_by_tag('type_a')

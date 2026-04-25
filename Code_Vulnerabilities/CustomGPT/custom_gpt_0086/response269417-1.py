
from django.db.models import Prefetch
from collections import defaultdict

# assuming you have your Item and Tag models defined
class Item(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    tags = models.ManyToManyField('Tag')

class Tag(models.Model):
    name = models.CharField(max_length=255)

def get_items_by_tags(item_type):
    # Prefetch related tags to minimize database hits
    items = Item.objects.filter(type=item_type).prefetch_related('tags')

    tag_dict = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    return dict(tag_dict)

# Usage example
items_by_tags = get_items_by_tags('type_a')
print(items_by_tags)

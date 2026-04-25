
from collections import defaultdict
from django.db.models import Prefetch

# Assuming you have imported your models
class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    tags = models.ManyToManyField('Tags')

class Tags(models.Model):
    name = models.CharField(max_length=100)

def get_items_by_tag(type_filter='type_a'):
    # Prefetch related tags for the items
    items = Item.objects.filter(type=type_filter).prefetch_related('tags')

    # Create a defaultdict to gather items by tags
    tag_dict = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    return dict(tag_dict)

# Usage
tagged_items = get_items_by_tag()
print(tagged_items)

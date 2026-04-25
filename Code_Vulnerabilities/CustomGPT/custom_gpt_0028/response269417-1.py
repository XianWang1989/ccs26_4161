
from collections import defaultdict
from django.db.models import Prefetch

# Assuming you have the following models:
class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    tags = models.ManyToManyField('Tag')

class Tag(models.Model):
    name = models.CharField(max_length=100)

# In your view:
def get_items_by_tags(type_filter):
    # Prefetch related tags to optimize queries
    items = Item.objects.filter(type=type_filter).prefetch_related('tags')

    # Create a dictionary to hold the tags and their corresponding items
    tags_dict = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tags_dict[tag.name].append(item)

    return tags_dict

# Example Usage
items_by_tags = get_items_by_tags('type_a')
print(items_by_tags)

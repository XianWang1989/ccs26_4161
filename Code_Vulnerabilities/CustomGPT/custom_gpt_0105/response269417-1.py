
from django.db.models import Prefetch
from collections import defaultdict

# Assuming you have a Tags model defined
class Tags(models.Model):
    name = models.CharField(max_length=100)

# Your Item model
class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tags)

# View to get items and relate them to tags
def get_items_with_tags(type_filter):
    # Prefetch related tags to minimize database queries
    items = Item.objects.filter(type=type_filter).prefetch_related('tags')

    # Create a default dictionary to hold tags and associated items
    tag_dict = defaultdict(list)

    # Build the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    return dict(tag_dict)

# Usage
result = get_items_with_tags('type_a')
print(result)

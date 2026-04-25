
from collections import defaultdict
from django.db.models import Prefetch

# Assuming you have a Tags model defined as follows:
class Tags(models.Model):
    name = models.CharField(max_length=100)

# Your Item model as provided
class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tags)

def get_items_by_tags(type_filter):
    # Get items with prefetch for tags
    items = Item.objects.filter(type=type_filter).prefetch_related('tags')

    # Create a defaultdict to hold items by tag name
    tag_dict = defaultdict(list)

    # Iterate through items and populate the tag_dict
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    return dict(tag_dict)

# Example usage
tagged_items = get_items_by_tags('type_a')
print(tagged_items)

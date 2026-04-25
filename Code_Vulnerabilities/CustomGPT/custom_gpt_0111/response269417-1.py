
from collections import defaultdict
from django.db.models import Prefetch

# Your Item model
class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    tags = models.ManyToManyField('Tags')

# Your Tags model
class Tags(models.Model):
    name = models.CharField(max_length=100)

# In your view
def get_items_by_tags(type_filter):
    # Fetch items with related tags using prefetch_related
    items = Item.objects.filter(type=type_filter).prefetch_related('tags')

    # Create a dictionary to hold tags as keys and a list of items as values
    tag_to_items = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_to_items[tag.name].append(item)

    return dict(tag_to_items)

# Example usage
result = get_items_by_tags('type_a')
print(result)

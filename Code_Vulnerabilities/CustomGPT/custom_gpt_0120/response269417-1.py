
from django.db.models import Prefetch
from collections import defaultdict

# Assuming you have a Tags model
class Tags(models.Model):
    name = models.CharField(max_length=100)

# Your existing Item model
class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tags)

# In your view
def get_items_with_tags(type_value):
    # Prefetch tags to avoid N+1 queries
    items = Item.objects.filter(type=type_value).prefetch_related('tags')

    # Initialize a defaultdict for automatic list creation
    tag_to_items = defaultdict(list)

    # Iterate over items and relate them to their tags
    for item in items:
        for tag in item.tags.all():
            tag_to_items[tag.name].append(item)

    return tag_to_items

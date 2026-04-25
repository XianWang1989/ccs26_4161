
from collections import defaultdict
from django.db.models import Prefetch

# Assuming you have a Tag model
class Tag(models.Model):
    name = models.CharField(max_length=100)

# Your existing Item model
class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)

# In your view
def get_items_by_tags(type_filter):
    # Fetch items with the specified type along with their tags using prefetch_related
    items = Item.objects.filter(type=type_filter).prefetch_related('tags')

    # Initialize a defaultdict to hold tags and corresponding items
    tag_to_items = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_to_items[tag.name].append(item)

    return dict(tag_to_items)

# Example usage
tagged_items = get_items_by_tags('type_a')
print(tagged_items)

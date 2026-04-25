
from collections import defaultdict
from django.db.models import Prefetch

# Assuming you have a Tags model related to your Item model.
class Tags(models.Model):
    name = models.CharField(max_length=100)

class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tags)

# In your view
def get_items_by_tags():
    # Filter items by type and prefetch related tags to minimize database queries
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a dictionary to hold tags and their associated items
    tag_dict = defaultdict(list)

    # Loop through items and organize them by tags
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    return dict(tag_dict)

# Example usage:
tagged_items = get_items_by_tags()
print(tagged_items)


from collections import defaultdict
from django.db.models import Prefetch

# Assuming you have a Tags model defined
class Tags(models.Model):
    name = models.CharField(max_length=100)

class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tags)

# Your view function
def my_view(request):
    # Filter items by type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Prepare a dictionary to hold tags and their associated items
    tag_to_items = defaultdict(list)

    for item in items:
        for tag in item.tags.all():
            tag_to_items[tag.name].append(item)

    return tag_to_items

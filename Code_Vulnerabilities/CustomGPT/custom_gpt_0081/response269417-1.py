
from collections import defaultdict
from django.db.models import Prefetch

# Assuming the models are defined as follows
class Tags(models.Model):
    name = models.CharField(max_length=100)

class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tags)

# Your view function
def my_view(request):
    # Filter the items by type and prefetch the related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Initialize a defaultdict to hold our tags to items mapping
    tags_to_items = defaultdict(list)

    # Loop through items and populate the tags_to_items dictionary
    for item in items:
        for tag in item.tags.all():
            tags_to_items[tag.name].append(item)

    return tags_to_items

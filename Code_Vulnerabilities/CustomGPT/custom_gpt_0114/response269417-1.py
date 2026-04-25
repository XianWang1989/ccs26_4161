
from django.db.models import Prefetch
from collections import defaultdict

# Assuming you have your models set up as shown
class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    tags = models.ManyToManyField('Tags')

class Tags(models.Model):
    name = models.CharField(max_length=100)

# Your view function
def get_items_with_tags(request):
    # Step 1: Filter items by type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Step 2: Initialize a default dictionary to hold tags and their related items
    tag_to_items = defaultdict(list)

    # Step 3: Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_to_items[tag.name].append(item)

    return tag_to_items

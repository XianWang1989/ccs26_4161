
from django.db import models
from django.db.models import Prefetch, Count

# Models
class Item(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    tags = models.ManyToManyField('Tags')

class Tags(models.Model):
    name = models.CharField(max_length=255)

# View Function
def get_items_with_tags():
    # Prefetch related tags for items of type 'type_a'
    items = Item.objects.filter(type='type_a').prefetch_related('tags').annotate(tag_count=Count('tags'))

    tags_to_items = {}

    # Iterate through the items and build the dictionary
    for item in items:
        for tag in item.tags.all():
            if tag.name not in tags_to_items:
                tags_to_items[tag.name] = []
            tags_to_items[tag.name].append(item)

    return tags_to_items

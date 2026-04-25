
from django.db import models

class Tags(models.Model):
    name = models.CharField(max_length=100)

class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tags)

# In your view
def get_items_with_tags():
    # First, filter the items based on type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Build a dictionary to relate tags to items
    tag_to_items = {}

    for item in items:
        for tag in item.tags.all():
            if tag.name not in tag_to_items:
                tag_to_items[tag.name] = []
            tag_to_items[tag.name].append(item)

    return tag_to_items


from collections import defaultdict

# Assuming your Item model looks like this:
class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    tags = models.ManyToManyField('Tags')

class Tags(models.Model):
    name = models.CharField(max_length=100)

def get_items_with_tags():
    # Filter items by type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a dictionary to relate tags to items
    tags_dict = defaultdict(list)

    for item in items:
        for tag in item.tags.all():
            tags_dict[tag.name].append(item)

    return dict(tags_dict)

# Use the function in your view
tags_to_items = get_items_with_tags()

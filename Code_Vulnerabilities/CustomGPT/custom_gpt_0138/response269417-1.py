
from collections import defaultdict
from django.db.models import Prefetch

# Assuming your models are defined like this
class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    tags = models.ManyToManyField('Tag')

class Tag(models.Model):
    name = models.CharField(max_length=100)

# In your view
def get_items_by_tags(request):
    # Prefetch related tags for items of type 'type_a'
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a defaultdict to hold tags and their associated items
    tag_dict = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    return dict(tag_dict)


from collections import defaultdict
from django.db.models import Prefetch

# Assuming you have a model for Tags
class Tags(models.Model):
    name = models.CharField(max_length=255)

# Your existing Item model
class Item(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tags)

# In your view
def get_items_by_tags(request):
    # Get items of a specific type while prefetching the related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a dictionary to hold tags with their related items
    tag_dict = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    return tag_dict

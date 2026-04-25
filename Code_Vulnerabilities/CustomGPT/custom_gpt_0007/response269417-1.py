
from collections import defaultdict
from django.db.models import Prefetch

# Assuming you have a model defined for Tags
class Tags(models.Model):
    name = models.CharField(max_length=100)

# Your Item model
class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tags)

# In your view
def get_items_with_tags(request):
    # Fetch items of a specific type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a defaultdict to store tags relating to items
    tag_dict = defaultdict(list)

    # Iterate through the items and populate the tag_dict
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    # Convert defaultdict to a regular dict if you prefer
    tag_dict = dict(tag_dict)

    return tag_dict

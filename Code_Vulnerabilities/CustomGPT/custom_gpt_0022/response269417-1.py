
from collections import defaultdict
from django.db.models import Prefetch

# Assuming your Tags model is defined as follows:
class Tags(models.Model):
    name = models.CharField(max_length=100)

# Your Item model
class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tags)

# Your view function
def get_items_with_tags(request):
    # Fetch items of a specific type along with their related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    tag_item_map = defaultdict(list)

    # Build the dictionary relating tags to items
    for item in items:
        for tag in item.tags.all():
            tag_item_map[tag.name].append(item)

    # Convert to a regular dict if needed
    tag_item_map = dict(tag_item_map)

    return tag_item_map

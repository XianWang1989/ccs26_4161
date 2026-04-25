
from django.db.models import Prefetch
from collections import defaultdict

# Assuming your model looks like this:
class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    tags = models.ManyToManyField('Tags')

# In your view:
def get_items_with_tags(request):
    type_filter = 'type_a'

    # Prefetch related tags for items of the specific type
    items = Item.objects.filter(type=type_filter).prefetch_related('tags')

    # Create a dictionary to hold the tags and their corresponding items
    tag_to_items = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_to_items[tag.name].append(item)

    return tag_to_items

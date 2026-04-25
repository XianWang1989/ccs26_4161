
from collections import defaultdict
from django.db.models import Prefetch

# Assuming you have a Tags model
class Tags(models.Model):
    name = models.CharField(max_length=100)

# Your modified view
def your_view(request):
    # Prefetch items related to the desired type and their tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a dictionary that maps tag names to lists of items
    tag_to_items = defaultdict(list)

    for item in items:
        for tag in item.tags.all():
            tag_to_items[tag.name].append(item)

    return tag_to_items

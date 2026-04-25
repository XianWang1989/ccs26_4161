
from collections import defaultdict
from django.db.models import Prefetch

# Assuming you have a Tags model defined
class Tags(models.Model):
    name = models.CharField(max_length=100)

class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tags)

# In your view
def get_items_by_tags(request):
    # Filter items by type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Initialize a default dictionary
    tag_dict = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    return dict(tag_dict)  # Convert to a regular dict if needed

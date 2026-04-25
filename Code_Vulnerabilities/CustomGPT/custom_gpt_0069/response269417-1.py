
from django.db.models import Prefetch
from collections import defaultdict

# Assuming you have a model for Tags also defined
class Tags(models.Model):
    name = models.CharField(max_length=100)

class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tags)

# In your view
def get_items_by_tags(request):
    # Prefetch the related tags for 'type_a' items
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    tag_dict = defaultdict(list)

    # Build the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    return tag_dict

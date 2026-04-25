
from collections import defaultdict
from django.db.models import Prefetch

# Your model
class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    tags = models.ManyToManyField('Tags')

class Tags(models.Model):
    name = models.CharField(max_length=100)

# View function
def your_view(request):
    # Filter items by type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a default dictionary to hold tags and their related items
    tag_dict = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    # Convert to a standard dictionary if required
    result = dict(tag_dict)

    return result  # Return this dictionary for your template or API response

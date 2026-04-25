
from django.db.models import Prefetch
from collections import defaultdict

# Assuming your Tags model looks like this
class Tags(models.Model):
    name = models.CharField(max_length=100)

# View to filter items by type and create the tags-to-items dictionary
def get_items_by_tags(request):
    # Filter items by type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a dictionary to map tags to items
    tags_dict = defaultdict(list)

    # Populate the dictionary
    for item in items:
        for tag in item.tags.all():
            tags_dict[tag.name].append(item)

    return tags_dict

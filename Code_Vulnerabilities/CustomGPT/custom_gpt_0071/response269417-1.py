
from django.db.models import Prefetch
from collections import defaultdict

# Assuming your Tags model is defined properly
class Tag(models.Model):
    name = models.CharField(max_length=100)

class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)

def get_items_by_tags(type_filter):
    # Prefetch related tags to avoid additional queries
    items = Item.objects.prefetch_related('tags').filter(type=type_filter)

    # Using defaultdict to create a dictionary of tags to items
    tags_dict = defaultdict(list)

    for item in items:
        for tag in item.tags.all():
            tags_dict[tag.name].append(item)

    return dict(tags_dict)  # Convert defaultdict back to a regular dict

# Example usage
result = get_items_by_tags('type_a')

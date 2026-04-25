
from django.db.models import Prefetch
from collections import defaultdict

# Assuming you have a model for Tags
class Tags(models.Model):
    name = models.CharField(max_length=100)

def get_tagged_items(view_type):
    # Filter the items and prefetch related tags
    items = Item.objects.filter(type=view_type).prefetch_related('tags')

    # Create a dictionary to hold tags as keys and list of items as values
    tag_dict = defaultdict(list)

    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    return dict(tag_dict)

# Example usage
tagged_items = get_tagged_items('type_a')
print(tagged_items)

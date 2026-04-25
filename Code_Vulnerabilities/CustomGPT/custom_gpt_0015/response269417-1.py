
from django.db.models import Prefetch
from collections import defaultdict

# Assume Tags is your ManyToMany relationship class
class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    tags = models.ManyToManyField('Tags')

def get_items_by_tag(type_value):
    # Prefetch tags for efficiency
    items = Item.objects.filter(type=type_value).prefetch_related('tags')

    tag_dict = defaultdict(list)

    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    return tag_dict

# Usage
result = get_items_by_tag('type_a')
print(result)

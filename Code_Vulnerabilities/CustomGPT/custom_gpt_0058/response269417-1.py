
from django.db.models import Prefetch
from collections import defaultdict

# Assuming you have the Tags model defined like this
class Tags(models.Model):
    name = models.CharField(max_length=100)

# Your item filtering and prefetching
items = Item.objects.prefetch_related('tags').filter(type='type_a')

# Initialize a dictionary to hold tags and corresponding items
tag_to_items = defaultdict(list)

# Populate the dictionary
for item in items:
    for tag in item.tags.all():
        tag_to_items[tag.name].append(item)

# Now tag_to_items will hold the desired output
print(dict(tag_to_items))

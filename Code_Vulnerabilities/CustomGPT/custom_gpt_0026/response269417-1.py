
from collections import defaultdict
from django.db.models import Prefetch

# Assuming you have a Tags model defined similar to:
class Tags(models.Model):
    name = models.CharField(max_length=50)

# Retrieve all relevant items with their tags
items = Item.objects.filter(type='type_a').prefetch_related('tags')

# Create a dictionary to hold the tags and their associated items
tag_dict = defaultdict(list)

# Populate the dictionary
for item in items:
    for tag in item.tags.all():
        tag_dict[tag.name].append(item)

# The tag_dict now contains the desired structure
print(tag_dict)

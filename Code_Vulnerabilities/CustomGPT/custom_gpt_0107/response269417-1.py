
from collections import defaultdict
from django.db.models import Prefetch

# Assuming you have a Tags model
class Tags(models.Model):
    name = models.CharField(max_length=255)

# Fetch items of a certain type with their related tags
items = Item.objects.filter(type='type_a').prefetch_related('tags')

# Create a dictionary to hold the tags and associated items
tags_dict = defaultdict(list)

# Populate the dictionary
for item in items:
    for tag in item.tags.all():
        tags_dict[tag.name].append(item)

# Convert defaultdict back to a regular dict if needed
tags_dict = dict(tags_dict)

# Now, tags_dict contains the desired mapping
print(tags_dict)

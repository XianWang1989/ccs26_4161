
from collections import defaultdict
from django.db.models import Prefetch

# Assuming you have already defined your Tags model
class Tags(models.Model):
    name = models.CharField(max_length=255)

# Fetch the items and prefetch related tags
items = Item.objects.filter(type='type_a').prefetch_related('tags')

# Create a dictionary to hold the tags and their corresponding items
tag_to_items = defaultdict(list)

# Iterate through the items and populate the dictionary
for item in items:
    for tag in item.tags.all():
        tag_to_items[tag.name].append(item)

# At this point, tag_to_items will have the structure you want
# Here's how it will look like:
# {
#    'tag1': [item1, item2, item5],
#    'tag2': [item1, item4],
#    'tag3': [item3, item5]
# }

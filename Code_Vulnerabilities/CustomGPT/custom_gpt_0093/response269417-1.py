
from django.db.models import Prefetch
from collections import defaultdict

# Assuming you have a Tags model
class Tags(models.Model):
    name = models.CharField(max_length=100)

# Fetch items of a specific type and prefetch related tags
items = Item.objects.filter(type='type_a').prefetch_related('tags')

# Create a dictionary to map tags to items
tagged_items = defaultdict(list)

# Populate the dictionary
for item in items:
    for tag in item.tags.all():
        tagged_items[tag.name].append(item)

# Convert defaultdict to a regular dict if necessary
tagged_items = dict(tagged_items)

# Output should look like:
# {
#     'tag1': [item1, item2, item5],
#     'tag2': [item1, item4],
#     'tag3': [item3, item5]
# }

# You can now use tagged_items as needed

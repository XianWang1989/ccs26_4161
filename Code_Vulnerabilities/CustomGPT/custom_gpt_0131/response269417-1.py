
from django.db.models import Prefetch

# Assuming you have a Tag model
class Tag(models.Model):
    name = models.CharField(max_length=100)

# Query to get items of type 'type_a' and prefetch related tags
items = Item.objects.filter(type='type_a').prefetch_related('tags')

# Initialize an empty dictionary to store the tag-item mapping
tag_to_items = {}

# Iterate through the items and build the dictionary
for item in items:
    for tag in item.tags.all():  # Using the cached relation
        if tag.name not in tag_to_items:
            tag_to_items[tag.name] = []
        tag_to_items[tag.name].append(item)

# Now tag_to_items contains the desired mapping of tags to items
print(tag_to_items)


from django.db.models import Prefetch
from collections import defaultdict

# Assuming you have a Tag model like this:
class Tag(models.Model):
    name = models.CharField(max_length=100)

# Modifying your filtering process and prefetching related tags
items = Item.objects.filter(type='type_a').prefetch_related('tags')

# Creating a dictionary to relate tags to items
tag_to_items = defaultdict(list)

for item in items:
    for tag in item.tags.all():
        tag_to_items[tag.name].append(item)

# Now, tag_to_items holds the desired structure
print(dict(tag_to_items))

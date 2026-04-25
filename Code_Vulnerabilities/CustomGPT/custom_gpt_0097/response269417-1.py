
from django.db.models import Prefetch
from .models import Item, Tag

# Get the items filtered by type and prefetch related tags
items = Item.objects.filter(type='type_a').prefetch_related('tags')

tag_dict = {}

for item in items:
    for tag in item.tags.all():
        if tag.name not in tag_dict:
            tag_dict[tag.name] = []
        tag_dict[tag.name].append(item)

# tag_dict now contains the desired format

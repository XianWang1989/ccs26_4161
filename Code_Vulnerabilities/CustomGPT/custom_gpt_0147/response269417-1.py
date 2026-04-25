
from django.db import models
from django.shortcuts import render

# Define models
class Tags(models.Model):
    name = models.CharField(max_length=100)

class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tags)

# View function
def item_view(request):
    # Filter items by type and prefetch related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    tags_to_items = {}

    # Build the dictionary
    for item in items:
        for tag in item.tags.all():
            if tag.name not in tags_to_items:
                tags_to_items[tag.name] = []
            tags_to_items[tag.name].append(item)

    # You can now use tags_to_items for rendering or further processing
    return render(request, 'template.html', {'tags_to_items': tags_to_items})

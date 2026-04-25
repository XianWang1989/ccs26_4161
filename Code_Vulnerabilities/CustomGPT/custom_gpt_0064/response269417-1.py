
from collections import defaultdict
from django.shortcuts import render

# Assuming the model classes are already defined.
class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    tags = models.ManyToManyField('Tags')

class Tags(models.Model):
    name = models.CharField(max_length=100)

def my_view(request):
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    tag_to_items = defaultdict(list)

    for item in items:
        for tag in item.tags.all():
            tag_to_items[tag.name].append(item)

    return render(request, 'template.html', {'tag_to_items': tag_to_items})

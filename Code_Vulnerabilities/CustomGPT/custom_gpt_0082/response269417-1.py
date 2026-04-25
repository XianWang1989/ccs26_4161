
from django.db.models import Prefetch
from collections import defaultdict

# Assume you have a model structure
class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    tags = models.ManyToManyField('Tags')

class Tags(models.Model):
    name = models.CharField(max_length=100)

# In your view
def my_view(request):
    # Fetch items of a specific type with related tags
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Initialize a defaultdict to hold the tag-item mapping
    tag_item_dict = defaultdict(list)

    # Build the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_item_dict[tag.name].append(item)

    # Convert defaultdict to a regular dict if needed
    tag_item_dict = dict(tag_item_dict)

    # Now you can use tag_item_dict as needed
    return render(request, 'my_template.html', {'tag_item_dict': tag_item_dict})

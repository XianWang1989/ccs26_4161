
from django.db.models import Prefetch, Count
from collections import defaultdict

# Assuming you already have your Item and Tag models defined as mentioned 
class Tag(models.Model):
    name = models.CharField(max_length=100)

# In your view, you can do something like this:

def your_view(request):
    # Filter items by the desired type
    items = Item.objects.filter(type='type_a').prefetch_related('tags')

    # Create a defaultdict to store our tags
    tag_dict = defaultdict(list)

    # Loop through each item and construct the dictionary
    for item in items:
        for tag in item.tags.all():
            tag_dict[tag.name].append(item)

    # Now tag_dict contains the mapping of tags to items
    return render(request, 'your_template.html', {'tag_dict': tag_dict})

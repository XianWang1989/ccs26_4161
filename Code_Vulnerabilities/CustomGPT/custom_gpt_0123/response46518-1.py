
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone

def your_view_name(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))

            # Update item status date
            item.current_item_status_date = timezone.now()
            item.save()

            return JsonResponse({'message': 'Item updated successfully.'})

    else:
        form = forms.ItemForm(instance=item)

    return render(request, 'your_template.html', {'form': form, 'item': item})

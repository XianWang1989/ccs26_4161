
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

def your_view(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid() and request.POST.get('save_item') is not None:
            form.save()
            request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))
            return JsonResponse({'message': 'Item updated successfully.'})

        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'message': 'Status date updated successfully.'})

    # Handle GET or invalid form submissions
    form = forms.ItemForm(instance=item)
    return render(request, 'example.html', {'form': form, 'item': item})

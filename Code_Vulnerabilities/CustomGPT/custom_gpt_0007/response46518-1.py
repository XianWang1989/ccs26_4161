
from django.http import JsonResponse
from django.shortcuts import render

def edit_order_view(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid() and save_item is not None:
            form.save(True)
            request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))
            # You might want to handle this case differently if this is meant to close the form
            return JsonResponse({'success': True, 'message': "Item updated successfully."})

        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'success': True, 'current_status_date': item.current_item_status_date})

    else:
        form = forms.ItemForm(instance=item)

    return render(request, 'edit_order.html', {'form': form, 'item': item})

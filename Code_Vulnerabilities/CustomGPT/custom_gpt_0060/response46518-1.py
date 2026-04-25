
from django.http import JsonResponse

if request.method == 'POST':
    form = forms.ItemForm(request.POST, instance=item)
    if form.is_valid() and save_item is not None:
        form.save(True)
        request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))

        # Return a JSON response for AJAX
        return JsonResponse({'status': 'success', 'message': 'Item updated successfully.'})

    if request.POST.get('save_status'):
        item.current_item_status_date = date.today()
        item.save()

        # Return a JSON response just for the status update
        return JsonResponse({'status': 'success', 'message': 'Status date updated successfully.'})

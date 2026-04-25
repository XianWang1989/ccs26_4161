
from django.http import JsonResponse

if request.method == 'POST':
    if request.POST.get('save_status'):
        item.current_item_status_date = date.today()
        item.save()
        return JsonResponse({'message': 'Status updated successfully.', 'new_date': item.current_item_status_date.isoformat()})
    else:
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))
            return JsonResponse({'message': 'Item updated successfully.'})

    return JsonResponse({'error': 'Invalid form submission.'})


from django.http import JsonResponse

if request.method == 'POST':
    if request.POST.get('save_status'):
        item.current_item_status_date = date.today()
        item.save()
        return JsonResponse({'status': 'success', 'message': f'Item {item.tiptop_id} status updated successfully.'})

    form = forms.ItemForm(request.POST, instance=item)
    if form.is_valid() and save_item is not None:
        form.save()
        request.user.message_set.create(message=f"Item {item.tiptop_id} has been updated successfully.")
        return JsonResponse({'status': 'success', 'message': 'Form updated successfully.'})

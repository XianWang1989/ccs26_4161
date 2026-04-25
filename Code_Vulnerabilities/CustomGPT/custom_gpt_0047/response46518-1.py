
from django.http import JsonResponse

if request.method == 'POST':
    form = forms.ItemForm(request.POST, instance=item)
    if form.is_valid() and save_item is not None:
        form.save()
        request.user.message_set.create(message=f"Item {item.tiptop_id} has been updated successfully.")
        return JsonResponse({'success': True, 'message': "Item updated successfully."})

    if request.POST.get('save_status'):
        item.current_item_status_date = date.today()
        item.save()
        return JsonResponse({'success': True, 'message': "Status date updated."})


from django.http import JsonResponse

if request.method == 'POST':
    form = forms.ItemForm(request.POST, instance=item)
    if form.is_valid():
        form.save()
        request.user.message_set.create(message=f"Item {item.tiptop_id} has been updated successfully.")

        # Return a JSON response on form save
        return JsonResponse({'status': 'success', 'message': 'Item updated successfully.'})

    if request.POST.get('save_status'):
        item.current_item_status_date = date.today()
        item.save()

        # Return a JSON response for status update
        return JsonResponse({'status': 'success', 'message': 'Status date updated successfully.'})

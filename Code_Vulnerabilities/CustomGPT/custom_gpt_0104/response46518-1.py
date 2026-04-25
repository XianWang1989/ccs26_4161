
from django.http import JsonResponse

if request.method == 'POST':
    form = forms.ItemForm(request.POST, instance=item)

    if form.is_valid() and request.POST.get('save_item') is not None:
        form.save(True)
        request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))

        return JsonResponse({'status': 'success', 'message': f"Item {item.tiptop_id} has been updated successfully."})

    if request.POST.get('save_status'):
        item.current_item_status_date = date.today()
        item.save()

        return JsonResponse({'status': 'success', 'message': "Item status date updated successfully."})

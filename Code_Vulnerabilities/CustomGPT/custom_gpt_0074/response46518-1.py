
from django.http import JsonResponse

if request.method == 'POST':
    form = forms.ItemForm(request.POST, instance=item)
    if form.is_valid() and save_item is not None:
        form.save(True)
        request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))
        response_data = {'message': "Item updated successfully."}
        return JsonResponse(response_data)

    if request.POST.get('save_status'):
        item.current_item_status_date = date.today()
        item.save()
        response_data = {'message': "Status date updated successfully."}
        return JsonResponse(response_data)

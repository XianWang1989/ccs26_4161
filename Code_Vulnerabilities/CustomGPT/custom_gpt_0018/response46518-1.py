
from django.http import JsonResponse

if request.method == 'POST':
    form = forms.ItemForm(request.POST, instance=item)
    if form.is_valid() and save_item is not None:
        form.save(True)
        request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))

        # This will send a success response
        return JsonResponse({"status": "success"})
    elif request.POST.get('save_status'):
        item.current_item_status_date = date.today()
        item.save()

        # Return a response indicating success
        return JsonResponse({"status": "status_updated"})

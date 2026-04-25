
from django.http import JsonResponse

def your_view_name(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)

        if form.is_valid() and save_item is not None:
            form.save()
            request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))
            return JsonResponse({'status': 'success'})

        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'status': 'status updated'})

    # Handle GET or other request types
    ...

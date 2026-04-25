
from django.http import JsonResponse
from django.views.decorators.http import require_POST

@require_POST
def edit_order(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid() and 'save_item' in request.POST:
            form.save()
            request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))
            return JsonResponse({'status': 'success', 'message': 'Item updated'}, status=200)

        if 'save_status' in request.POST:
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'status': 'success', 'message': 'Status updated'}, status=200)

    return JsonResponse({'status': 'error', 'message': 'Invalid form'}, status=400)
